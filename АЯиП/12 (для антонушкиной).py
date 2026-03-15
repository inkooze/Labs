"""
Работа №12 (По требованиям Антонушкиной) - Вариант 1 - Словари
- Вариант 1: Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}. Объедините их в один словарь dictionary_main при помощи встроенных функций языка Python, затем добавьте новый элемент с ключом 'e' и значением 1000
"""

n1 = int(input('Введие кол-во элементов для dictionary_1... '))
dictionary_1 = {}
for i in range(n1):
	key, value = input('Вводи пару... ').split()
	dictionary_1[key] = int(value)

n2 = int(input('Введие кол-во элементов для dictionary_2... '))
dictionary_2 = {}
for i in range(n2):
	key, value = input('Вводи пару... ').split()
	dictionary_2[key] = int(value)

dictionary_main = dictionary_1.copy()
dictionary_main.update(dictionary_2)

dictionary_main['e'] = 1000

for key, value in dictionary_main.items():
	print(f'{ key }: { value }')