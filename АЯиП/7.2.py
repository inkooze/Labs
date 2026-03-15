'''
Работа №7.2 - Проектирование алгоритмов и программ с использованием цикла с предусловием
- Значения функций f1(x) = (x + 1) / 2 * cos(x / 3), f2(x) = (x + 2) / 3 * sin(x / 4), определены в точках x = x0(hx)xn. Определить расстояние между максимальными значениями функций f1(x) и f2(x).
'''''

from math import sin, cos

f1 = lambda x: (x + 1) / 2 * cos(x / 3)
f2 = lambda x: (x + 2) / 3 * sin(x / 4)

x0, hx, xn = map(int, input('Введи x0, hx и xn через пробел... ').split())
f1max, f2max = -10**9, -10**9

while (x0 < xn) == (hx > 0):
	f1max = max(f1max, F1 := f1(x0))
	f2max = max(f2max, F2 := f2(x0))

	print(f'x = { x0 }, f1 = { F1 }, f2 = { F2 }')

	x0 += hx

print('\nРасстояние между f1max и f2max = ', abs(f1max - f2max))