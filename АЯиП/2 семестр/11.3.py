'''
Работа №11.3 - Вариант 16 - Кортежи
- Удалить первое появление определенного элемента из кортежа по значению и вывести кортеж без него. Если элемента в кортеже нет, вывести кортеж в исходном виде. Можно использовать срезы и операцию + для кортежей.
'''''

nums = 1, 2, 3, 4, 5
targetNum = 3

if targetNum in nums:
	targetNumIndex = nums.index(targetNum)
	print(nums[:targetNumIndex] + nums[targetNumIndex + 1:])
else:
	print(nums)