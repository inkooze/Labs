'''
Работа №9 - Вариант 16 - Списки (одномерные массивы данных)
- В произвольно заданном одномерном массиве определить среднее значение всех элементов, значение которых превышает среднее значение.
'''''

arr = list(map(float, input('Введи элементы списка через пробел... ').split()))
arrMiddle = sum(arr) / len(arr)

targetArr = [i for i in arr if i > arrMiddle]


print(sum(targetArr) / len(targetArr))