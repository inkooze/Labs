"""
Работа №10 - Вариант 16 - Матрицы (двумерные массивы данных)
- Определить и поменять местами максимальное и минимальное значения двух квадратных матриц.

- Переменные:
	- a, b - матрицы;
	- na, nb - кол-во строк-столбцов (строк = столбцов, так как матрицы квадратные) матриц a и b соответственно;
	- temp - вспомогательная переменная для обмена;
	- i, j - параметры циклов;
	- amax, bmin - максимальный и минимальный элементы в матрицах a и b соответственно;
	- aimax, ajmax - индексы строки и столбца максимального элемента в матрице a;
	- bimin, bjmin - индексы строки и столбца минимального элемента в матрице b.
"""

na = int(input('Введи кол-во строк-столбцов (т.к. матрица квадратная) в матрице a... '))
nb = int(input('\nВведи кол-во строк-столбцов (т.к. матрица квадратная) в матрице b... '))

a = [[0] * na for _ in range(na)]
for i in range(na):
	for j in range(na):
		a[i][j] = int(input(f'a[{i}][{j}] = '))

print('\nМатрица a:')
for i in range(na):
	for j in range(na):
		print(a[i][j], end = '\t')
	print()

b = [[0] * nb for _ in range(nb)]
for i in range(nb):
	for j in range(nb):
		b[i][j] = int(input(f'b[{i}][{j}] = '))

print('\nМатрица b:')
for i in range(nb):
	for j in range(nb):
		print(b[i][j], end = '\t')
	print()

amax = a[0][0]
aimax = 0
ajmax = 0
for i in range(na):
	for j in range(na):
		if a[i][j] > amax:
			amax = a[i][j]
			aimax = i
			ajmax = j

bmin = b[0][0]
bimin = 0
bjmin = 0
for i in range(nb):
	for j in range(nb):
		if b[i][j] < bmin:
			bmin = b[i][j]
			bimin = i
			bjmin = j

print(f'\nМаксимальный элемент в матрице a: a[{aimax}][{ajmax}] = {amax}')
print(f'Минимальный элемент в матрице b: b[{bimin}][{bjmin}] = {bmin}')

temp = a[aimax][ajmax]
a[aimax][ajmax] = b[bimin][bjmin]
b[bimin][bjmin] = temp

print('\nМатрица a после изменений:')
for i in range(na):
	for j in range(na):
		print(a[i][j], end = '\t')
	print()

print('\nМатрица b после изменений:')
for i in range(nb):
	for j in range(nb):
		print(b[i][j], end = '\t')
	print()