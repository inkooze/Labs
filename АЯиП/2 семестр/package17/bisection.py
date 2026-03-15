def bisection(f, a, b):
    if f(a) * f(b) >= 0:
        print('На концах интервала функция должна иметь разные знаки!')
        return None

    for i in range(100):
        c = (a + b) / 2
        if abs(f(c)) < 1e-6 or (b - a) / 2 < 1e-6:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print('Достигнуто максимальное число итераций!')
    return None