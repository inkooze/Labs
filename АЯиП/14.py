"""
Работа №14 - Вариант 16 - Подпрограммы
- Составить подпрограмму определения адресов элементов, значения которых лежат в пределах от p до q, в одномерном массиве. С помощью этой подпрограммы определить и вывести на экран адреса соответствующих элементов в столбцах двухмерной матрицы.
- Во всех заданиях ввод исходных и вывод результирующих матриц производить с помощью соответствующих подпрограмм пользователя!

- Переменные:
    - a - матрица;
    - n, m - её кол-во строк и столбцов соответственно;
    - p, q - левый и правый пределы отрезка;
    - i, j, el - параметры циклов;
    - bar - элементы j-го столбца матрицы.
"""

def InArr(n: int, m: int) -> list[list[int]]:
    print('\nСоздание матрицы:')
    a = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = int(input(f'a[{i}][{j}] = '))
    return a

def OutArr(a: list[list[int]]) -> None:
    print('\nМатрица:')
    for row in a:
        for i in row:
            print(i, end = '\t')
        print()

def InLimit(arr: list[int], l: int, p: float, q: float) -> list[int]:
    indexes = []
    for i in range(l):
        if p <= arr[i] <= q:
            indexes.append(i)
    return indexes

# / / /

n = int(input('Введи кол-во строк в матрице a... '))
m = int(input('Введи кол-во столбцов в матрице a... '))

a = InArr(n, m)
OutArr(a)

p = int(input('\nВведи левый предел p... '))
q = int(input('Введи правый предел q... '))

print(f'\nВошедшие в предел [{p}; {q}]:')
for j in range(m):
    bar = [0] * n
    for i in range(n):
        bar[i] = a[i][j]

    indexes = InLimit(bar, n, p, q)

    for el in indexes:
        print(f'a[{el}][{j}] = {a[el][j]}')