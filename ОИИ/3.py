from random import sample, randint
from functools import reduce
from pandas import ExcelWriter, DataFrame

# / / / / /

# 2.2.2
def accessoryDegrees(B, propertiesSet):
    degrees = []
    for A in propertiesSet:
        degrees.append(len(A & B) / len(A | B))

    return sorted(degrees, reverse = True)

# 2.2.4
def accessoryFunction(U, expertMarks):
    expertMarks = iter(expertMarks)
    matrix = [[1] * len(U) for _ in range(len(U))]
    for i in range(len(U) - 1):
        for j in range(i + 1, len(U)):
            matrix[i][j] = next(expertMarks)
            matrix[j][i] = 1 / matrix[i][j]

    wAll = []
    for row in matrix:
        wAll.append(reduce(lambda a, b: a * b, row) ** (1 / len(row)))

    wNormalized = []
    for w in wAll:
        wNormalized.append(w / sum(wAll))

    return matrix, wAll, wNormalized

# / / / / /

U = {'Умный', 'Старательный', 'Пунктуальный', 'Креативный', 'Общительный', 'Ленивый', 'Ответственный', 'Внимательный', 'Целеустремлённый', 'Самостоятельный'} # Св-ва объектов
B = {'Старательный', 'Пунктуальный', 'Ответственный', 'Внимательный', 'Целеустремлённый', 'Самостоятельный'} # Наиболее существенные св-ва

students = {'Студент №' + str(i): set(sample(list(U), randint(3, 5))) for i in range(1, 6 + 1)}

# / / / / /

# 2.1.1
studentsAccessoryDegrees = []
for studentU in students.values():
    studentsAccessoryDegrees.append(len(studentU & B) / len(studentU | B))

# 2.1.3
U = ['Персональный компьютер типа IBM PC', 'Ноутбук', 'Карманный персональный компьютер (КПК)'] # Объекты
expertMarks = iter([3, 5, 2])

matrix = [[1] * len(U) for _ in range(len(U))]
for i in range(len(U) - 1):
    for j in range(i + 1, len(U)):
        matrix[i][j] = next(expertMarks)
        matrix[j][i] = 1 / matrix[i][j]

# 2.1.4
wAll = []
for i in range(3):
    stolb = 1
    for row in matrix:
        stolb *= row[i]
    wAll.append(stolb ** (1 / 3))

wNormalized = []
for w in wAll:
    wNormalized.append(w / sum(wAll))

# Автообновление диаграммы
with ExcelWriter('3 (Степени принадлежности).xlsx', engine = 'xlsxwriter') as writer:
    # Запись данных в ячейки, чтобы по ним потом сделать диаграмму
    DataFrame({'Категория': U, 'Значение': wNormalized}).to_excel(writer, sheet_name = 'Лист1', index = False)

    # Создаём диаграмму
    chart = writer.book.add_chart({'type': 'column'})
    chart.add_series({
        'categories': '=Лист1!$A$2:$A$4',
        'values': '=Лист1!$B$2:$B$4',
        'name': 'Значения',
    })
    writer.sheets['Лист1'].insert_chart('D2', chart)

# / / / / /

print(f'''Частичная принадлежность строгих множеств друг другу: { studentsAccessoryDegrees }

Матрица парных сравнений, по шкале Саати, по надёжности:
{ '\n'.join(str(row) for row in matrix) }

По мощности:
{ '\n'.join(str(row) for row in accessoryFunction(U, [6, 8, 4])[0]) }

Расчёт функции принадлежности, используя косвенный метод:
w = {wAll}
μ = {wNormalized}
''')

# / / / / / / / / / /

# 2.2.3
print(accessoryDegrees(B, students.values()))

# 2.2.5
print(accessoryFunction(U, [3, 5, 2]), '\n', accessoryFunction(U, [6, 8, 4]))

nadezhnost = accessoryFunction(U, [3, 5, 2])[2]
moshnost = accessoryFunction(U, [6, 8, 4])[2]

dic = {
    'Персональный компьютер типа IBM PC': (nadezhnost[0], moshnost[0]),
    'Ноутбук': (nadezhnost[1], moshnost[1]),
    'Карманный персональный компьютер (КПК)': (nadezhnost[2], moshnost[2])
}

def otric(A):
    return 1 - A

def dizun(A, B):
    return max(A, B)

def konun(A, B):
    return min(A, B)

def implic(A, B):
    return min(1, 1 + B - A)

def pricel(A, B):
    return dizun(konun(A, otric(B)), konun(otric(A), B))


print()
for key, value in dic.items():
    A, B = value
    print(f'{key}:\nA: {A}, -A: {otric(A)}, B: {B}, -B: {otric(B)}, A&B: {konun(A, B)}, A|B: {dizun(A, B)}, A->B: {implic(A, B)}, A(+)B: {pricel(A, B)}\n')