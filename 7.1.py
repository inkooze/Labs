'''
Работа №7.1 - Цикл с предусловием
- То же самое задание, что и в 6.3, только цикл через while.
'''''

x0, hx, xn = map(float, input('Введи x0, hx и xn через пробел... ').split())
sum, prod = 0, 1

while (hx > 0 and x0 <= xn + hx / 2) or (hx < 0 and x0 >= xn - hx / 2):
	if 0 < x0 <= 6:
		y = 0.5 * x0
	elif -3 <= x0 <= 0:
		y = -x0
	else:
		y = 3

	sum += y
	prod *= y
	print(f'({ x0 }; { y })')

	x0 += hx

print(f'\nСумма: { sum }, произведение: { prod }')