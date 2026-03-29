# Отрицание
def NOT(A: float):
    return 1 - A

# Дизъюнкция
def OR(A, B):
    return max(A, B)

# Конъюнкция
def AND(A, B):
    return min(A, B)

# Импликация
def IMPLICATION(A, B):
    return min(1, 1 + B - A)

# Импликация Мамдани
def IMPLICATION1(A, B):
    return min(A, B)

# Импликация Лукасевача
def IMPLICATION2(A, B):
    return min(1, 1 - A + B)

# Импликация Ларсена
def IMPLICATION3(A, B):
    return A * B

# Импликация Гёделя
def IMPLICATION4(A, B):
    return 1 if A <= B else B

# Импликация по максиминному правилу
def IMPLICATION5(A, B):
    return max(min(A, B), 1 - A)

# Импликация по бинарному правилу
def IMPLICATION6(A, B):
    return min(max(1 - A, B), A)

# Сложение по модулю 2
def XOR(A, B):
    return OR(AND(A, NOT(B)), AND(NOT(A), B))