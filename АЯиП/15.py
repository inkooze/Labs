"""
Работа №15 - Вариант 16 - Строки
- В заданной последовательности символов заменить каждую последовательность из одинаковых символов длиной более трех на (k)s, где s – повторяющийся символ, k - число повторений.
- При выполнении данного задания не использовать другие типы данных (множества, списки и др.) Также нельзя пользоваться функцией split. Т.е. необходимо реализовать классический алгоритм работы со строками.
"""

string = 'aaabbbbbccbbbdddddddeeeeffghiiii'

subString = string[0]
for char in string + '\0':
	if subString[0] == char:
		subString += char
	else:
		if len(subString) > 3:
			string = string.replace(subString, str(len(subString)) + subString[0], 1)
		subString = char

print(string)