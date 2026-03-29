from random import sample, randint
from pandas import ExcelWriter
from package.excel import addChart
from package.calculating import accessoryDegrees, accessoryFunction, dictionaryOutput, matrixOutput
from package.logical import NOT, OR, AND, IMPLICATION, IMPLICATION1, IMPLICATION2, IMPLICATION3, IMPLICATION4, IMPLICATION5, IMPLICATION6, XOR

# / / /

allAtributes = {'Умный', 'Старательный', 'Пунктуальный', 'Креативный', 'Общительный', 'Ленивый', 'Ответственный', 'Внимательный', 'Целеустремлённый', 'Самостоятельный'}
strictAttributes = {'Старательный', 'Пунктуальный', 'Ответственный', 'Внимательный', 'Целеустремлённый', 'Самостоятельный'}

students = {'Студент №' + str(i): set(sample(list(allAtributes), randint(3, 5))) for i in range(1, 6 + 1)}

studentsAccessoryDegrees = accessoryDegrees(students, strictAttributes)

# / / /

objects = ['ПК (IBM PC)', 'Ноутбук', 'КПК']

durabilityMatrix, durabilityFunctions = accessoryFunction(len(objects), [3, 5, 2]) # Надёжность
powerMatrix, powerFunctions = accessoryFunction(len(objects), [6, 8, 4]) # Мощность

# / / /

# Автообновление диаграммы
with ExcelWriter('3 (Степени принадлежности).xlsx', engine = 'xlsxwriter') as file:
    lastChartLine = addChart(file, objects, durabilityFunctions, 0, 'column')
    addChart(file, objects, powerFunctions, lastChartLine, 'column')

# / / /

objectsFunctions = {}
for i in range(len(objects)):
    objectsFunctions[objects[i]] = durabilityFunctions[i], powerFunctions[i]

objectsLogical = {}
for key, value in objectsFunctions.items():
    A, B = value
    objectsLogical[key] = NOT(A), NOT(B), AND(A, B), AND(NOT(A), NOT(B)), OR(A, B), OR(NOT(A), NOT(B)), IMPLICATION(A, B), IMPLICATION1(A, B), IMPLICATION2(A, B), IMPLICATION3(A, B), IMPLICATION4(A, B), IMPLICATION5(A, B), IMPLICATION6(A, B), XOR(A, B), AND(A, NOT(B))

print(f'''- Все возможные свойства (качества, выбранные самостоятельно): { allAtributes }
- Наиболее существенные свойства (также выбранные самостоятельно): { strictAttributes }

Студенты и их качества (подобраны рандомно, каждому 3-5 качеств):
{ dictionaryOutput(students) }

- - - - - - - - - -

Частичная принадлежность строгих множеств друг другу:
{ dictionaryOutput(studentsAccessoryDegrees) }

- - - - - - - - - -

Матрицы парных сравнений на основе шкалы Саати, а также их функции принадлежности (по надёжности и мощности соответственно):
{ matrixOutput(durabilityMatrix) }
Функции принадлежности: { durabilityFunctions }

{ matrixOutput(powerMatrix) }
Функции принадлежности: { powerFunctions }

- - - - - - - - - -

Значения функций принадлежности (надёжность и мощность соответственно):
{ dictionaryOutput(objectsFunctions) }

Результат различных операций (логических связок) со значениями функций принадлежности:
{ dictionaryOutput(objectsLogical) }

- - - - - - - - - -
''')

logicalStatements = [
    'Самый ненадёжный',
    'Самый немощный',
    'Самый надёжный и мощный',
    'Самый ненадёжный и немощный',
    'Самый надёжный или мощный',
    'Самый ненадёжный или немощный',
    'Самый надёжный -> мощный (станд.)',
    'Самый надёжный -> мощный (Мамдани)',
    'Самый надёжный -> мощный (Лукасевач)',
    'Самый надёжный -> мощный (Ларсен)',
    'Самый надёжный -> мощный (Гёдель)',
    'Самый надёжный -> мощный (Максиминно)',
    'Самый надёжный -> мощный (Бинарно)',
    'Самый либо надёжный, либо мощный (строго)',
    'Самый надёжный, но немощный'
]

for i in range(len(logicalStatements)):
    sTname = ''
    sTvalue = 0

    for key, value in objectsLogical.items():
        if value[i] > sTvalue:
            sTname = key
            sTvalue = value[0]

    print(f'- { logicalStatements[i] }: { sTname } ({ sTvalue })')