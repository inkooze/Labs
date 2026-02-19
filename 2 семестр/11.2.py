'''
Работа №11.2 - Вариант 16 - 
- Входные данные программы: кортеж и некоторый элемент. Программа должна выводить кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно.
- Если элемента нет вовсе – вывести пустой кортеж.
- Если элемент встречается только один раз, то вывести кортеж, который начинается с него и идет до конца исходного.
'''''

nums = 1, 7, 2, 3, 4, 6, 7, 8, 4, 6, 7
targetNum = 7

startIndex = None
endIndex = None
for i in range(len(nums)):
	if nums[i] == targetNum:
		if startIndex:
			endIndex = i + 1
			break
		else:
			startIndex = i

print(nums[startIndex:endIndex] if startIndex or endIndex else ())