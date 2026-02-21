'''
Работа №13~ - Вариант 8 - Множества
- Вывести в возрастающем порядке все целые числа из диапазона 1..1000, представимые в виде n^2+m^2, где n>0, m>0.
'''''

targetNums = set()

for N in range(1, 1001):
	for n in range(1, 33):
		for m in range(1, 33):
			if N == m ** 2 + n ** 2:
				targetNums.add(N)

print(targetNums)