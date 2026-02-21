'''
Работа №10~ - Вариант 16 - Матрицы (двумерные массивы данных)
- Напишите программу, которая заполняет матрицу из N строк и M столбцов натуральными числами по спирали, как показано в примере. Спираль раскручивается по часовой стрелке.
- Входные данные: Входная строка содержит числа N и M ( 1 ≤ N , M ≤ 100 ), разделённые пробелом.
- Выходные данные: Программа должна вывести матрицу, заполненную заданным способом.
'''''

# Релиз кода сырой, не исправлялся, не оптимизировался, он просто существует.

i, j = map(int, input().split())
matrix = [[0] * j for _ in range(i)]

rule = 0  # 0 - вправо, 1 - вниз, 2 - влево, 3 - вверх
I, J = 0, 0
num, n = 1, i * j
loop0, loop1, loop2, loop3 = 0, 0, 0, 0

while num <= n:
    if rule == 0:
        if J < j - loop0:
            matrix[I][J] = num
            num += 1
            J += 1
        else:
            loop3 += 1
            I += 1
            J -= 1
            rule = 1

    elif rule == 1:
        if I < i - loop1:
            matrix[I][J] = num
            num += 1
            I += 1
        else:
            loop0 += 1
            I -= 1
            J -= 1
            rule = 2

    elif rule == 2:
        if J >= loop2:
            matrix[I][J] = num
            num += 1
            J -= 1
        else:
            loop1 += 1
            J += 1
            I -= 1
            rule = 3

    elif rule == 3:
        if I >= loop3:
            matrix[I][J] = num
            num += 1
            I -= 1
        else:
            loop2 += 1
            I += 1
            J += 1
            rule = 0

for row in matrix:
    print(*row, sep = '\t')