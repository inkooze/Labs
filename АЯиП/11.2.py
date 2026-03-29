"""
Работа №11.2 - Общий вариант - Кортежи
- Входные данные программы: кортеж и некоторый элемент. Программа должна выводить кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно:
	- Если элемента нет вовсе – вывести пустой кортеж.
	- Если элемент встречается только один раз, то вывести кортеж, который начинается с него и идет до конца исходного.

- Переменные:
	- nums - кортеж;
	- targetNum - элемент-ограничитель;
	- startIndex, endIndex - индекс начала и конца соответственно для среза итогового кортежа;
	- i - параметр цикла.
"""

numsCount = int(input('Укажи количество чисел... '))
nums = tuple(int(input(f'Введи { i + 1 } число... ')) for i in range(numsCount))
targetNum = int(input('Какое произведение искать... '))

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