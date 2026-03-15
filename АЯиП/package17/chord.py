def chord(f, a, b):
    if f(a) * f(b) >= 0:
        print('На концах интервала функция должна иметь разные знаки!')
        return None

    for i in range(100):
        x = a - f(a) * (b - a) / (f(b) - f(a))
        if abs(f(x)) < 1e-6:
            return x

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    print('Достигнуто максимальное число итераций!')
    return None