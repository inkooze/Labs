'''
Работа №8 - Вложенные циклы
- Разработать алгоритм и программу, осуществляющую табулирование заданной функции при изменении аргумента a от начального значения a0 до конечного значения an с постоянным шагом ha, т.е. a = a0(ha)an.
- Степени переменных сделать через циклы, а не через операцию или функцию возведения в степень!
'''''

a, ha, an = map(float, input('Введи a0, ha и an через пробел... ').split())

while (ha > 0 and a <= an + 1e-9) or (ha < 0 and a >= an - ha / 2):
	temps = 0
	if a < 0.4:
		for n in range(1, 10):
			tempa = a
			for _ in range(1, n):
				tempa *= a

			temps += a * a / (tempa - 5)
		Q = a / 3 * temps

	else:
		for n in range(1, 8):
			tempa_1 = a - 1
			for _ in range(1, n):
				tempa_1 *= a - 1

			temps += 1 + tempa_1 / n
		Q = (a + 1) / a * temps

	print(f'a = { a }, Q = { Q * 2 = }')
	a += ha