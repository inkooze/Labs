'''
Работа №9 - Вариант 16 - Списки (одномерные массивы данных)
- В произвольно заданном одномерном массиве определить среднее значение всех элементов, значение которых превышает 
среднее значение.
'''''

def mean(arr):
	return sum(arr) / len(arr) if arr else None

def superMean(arr):
	if not arr:
		return None
	arrMiddle = mean(arr)

	arr2 = [i for i in arr if i > arrMiddle]
	if not arr2:
		return None

	return mean(arr2)

print(superMean(list(map(float, input('Введи элементы списка через пробел... ').split()))))



# arr = list(map(float, input('Введи элементы списка через пробел... ').split()))
# arrMiddle = sum(arr) / len(arr)
#
# targetArr = [i for i in arr if i > arrMiddle]
#
# print(sum(targetArr) / len(targetArr))