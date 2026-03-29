from math import exp

# / / /

def triangleFunction(a, b, c, x):
    if a <= x <= b:
        return 1 - (b - x) / (b - a)
    elif b <= x <= c:
        return 1 - (x - b) / (c - b)
    else:
        return 0

def trapezoidFunction(a, b, c, d, x):
    if a <= x <= b:
        return 1 - (b - x) / (b - a)
    elif b <= x <= c:
        return 1
    elif c <= x <= d:
        return 1 - (x - c) / (d - c)
    else:
        return 0

def gaussFunction(c, omega, x):
    return round(exp(-((x - c) / omega) ** 2), 2)