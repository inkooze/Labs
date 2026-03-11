'''
Работа №16 - Вариант 6 (16) - Файлы (Бинарные файлы)
- Во всех вариантах заданий предусмотреть ввод пользователем количества компонент. Далее, записать компоненты в файл, закрыть файл. После этого заново открыть файл и считать из него компоненты так, как будто заранее неизвестно их число.
- Записать в файл оценки (в баллах), полученные некоторым студентом на экзаменах в течение всех сессий, и определить средний балл.
'''''

marksCount = int(input('Укажи количество чисел... '))
disciplines = tuple(input(f'{ i + 1 } дисциплина... ') for i in range(marksCount))
marks = tuple(input(f'Оценка за { disciplines[i] }... ') for i in range(marksCount))

with open(r'/radio_python/АЯиП/2 семестр/16.1 (Оценки).txt', 'a', encoding = 'UTF-8') as file:
	for i in range(marksCount):
		file.write(f'{ disciplines[i] }: { marks[i] }\n')

with open(r'/radio_python/АЯиП/2 семестр/16.1 (Оценки).txt', 'r', encoding = 'UTF-8') as file:
	marksSum = 0
	marksCount = 0

	for line in file:
		marksSum += int(line.split(': ')[1])
		marksCount += 1

print('\nСреднее арифметическое:', marksSum / marksCount)