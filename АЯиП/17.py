'''
Работа №17 - Вариант 16 - Модули
- Реализовать пакет для приближенного вычисления корня уравнения f(x)=0, имеющего на интервале (a; b) один-единственный корень, с использованием:
	- Метода половинного деления;
	- Метода итераций;
	- Метода хорд. При выборе вида функции.
- При выборе вида функции f(x) можно использовать меню или встроенную функцию eval() для динамического исполнения выражений из ввода.
'''''

import math
from package17 import *

# def main():
while True:
    method = input('\nВыбери метод для решения уравнения:\n1. Метод половинного деления;\n2. Метод хорд;\n3. Метод простых итераций.... ')

    if method == '1':
        expression = input('Введи f(x)... ')
        def f(x):
            return eval(expression, {'__builtins__': {}}, {'x': x, **math.__dict__})

        # try:
        #     f(0)
        # except:
        #     print('Ошибка в выражении функции.')
        #     # return
        #     break

        a, b = map(float, input('Укажи границы a, b через пробел... ').split())

        root = bisection(f, a, b)
        if root:
            print(f'Корень: {root:.8f}')
        else:
            print('Корень не найден...')

    elif method == '2':
        expression = input('Введи f(x)... ')
        def f(x):
            return eval(expression, {'__builtins__': {}}, {'x': x, **math.__dict__})

        # try:
        #     f(0)
        # except:
        #     print('Ошибка в выражении функции.')
        #     # return
        #     break

        a, b = map(float, input('Укажи границы a, b через пробел... ').split())

        root = chord(f, a, b)
        if root:
            print(f'Корень: {root:.8f}')
        else:
            print('Корень не найден...')

    elif method == '3':
        expression = input('Введи ф(x)... ')
        def phi(x):
            return eval(expression, {'__builtins__': {}}, {'x': x, **math.__dict__})

        # try:
        #     phi(0)
        # except:
        #     print('Ошибка в выражении функции.')
        #     # return
        #     break

        x0 = float(input('Укажи начальное приближение x0... '))

        root = iteration(phi, x0)
        if root:
            print(f'Корень: {root:.8f}')
        else:
            print('Корень не найден...')

    else:
        break

# if __name__ == "__main__":
#     main()