'''
Лабораторная работа 3-4 по МЛТА | Минин Р.Н., Цвигун К.Р.
'''''

debugFunctionVector = bin(int(input('Введите число от 0 до 255: ')))[2:].zfill(8)

SDNF, SKNF = [], []
T1, T0, S, L = '-', '-', '+', '+'

# / / / / /

# Построение таблицы истинности, заполнение SDNF и SKNF
print(f'''
Таблица истинности:
| x1 | x2 | x3 | f ({ int(debugFunctionVector, 2) }, { debugFunctionVector })''')

i = 0
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            if int(debugFunctionVector[i]):
                SDNF.append((['¬', ''][x1] + 'x1', ['¬', ''][x2] + 'x2', ['¬', ''][x3] + 'x3'))
            else:
                SKNF.append((['', '¬'][x1] + 'x1', ['', '¬'][x2] + 'x2', ['', '¬'][x3] + 'x3'))
            print('|', x1, ' |', x2, ' |', x3, ' |', debugFunctionVector[i])

            # Проверки на принадлежность к классам T0 и T1
            if x1 + x2 + x3 + int(debugFunctionVector[i]) == 4: T1 = '+'
            if x1 + x2 + x3 + int(debugFunctionVector[i]) == 0: T0 = '+'

            i += 1

# Проверка на принадлежность к классу S
for i in range(4):
    if debugFunctionVector[i] == debugFunctionVector[- i - 1]: S = '-'

# / / / / /

# Превращение в красивое СКНФ (указать истинный type) и СДНФ (не указывать type)
def prettyFunction(function, type = None, minimal = None):
    if type: # СКНФ, КНФ
        if debugFunctionVector == '00000000' and minimal:
            return '0'
        elif function:
            return '(' + ') & ('.join(['ⅴ'.join(x) for x in function]) + ')'
        else:
            return ''
    else: # СДНФ, ДНФ
        if debugFunctionVector == '11111111' and minimal:
            return '1'
        else:
            return ' ⅴ '.join([''.join(x) for x in function])

# Превращение итерируемого объекта в строку и удаление в ней символов '¬'. Например: ('¬x1', 'x2', '¬x3') -> 'x1x2x3'
bezcherti = lambda nabor: ''.join(nabor).replace('¬', '')
# Функция через lambda выше и закомментированная через def ниже буквально одно и то же
# def bezcherti(nabor):
#     return ''.join(nabor).replace('¬', '')

# Склейка функции
def gluing(function):
    for i in range(3):
        glued, beGlued = [], []
        for loop, hand in enumerate(function):
            for finger in function[loop:]:
                intersection = [i for i in hand if i in finger]

                if bezcherti(hand) == bezcherti(finger) and len(hand) - len(intersection) == 1:
                    beGlued.extend([hand, finger])
                    glued.append(intersection)

                if (hand not in beGlued + glued) and (finger == function[-1]):
                    glued.append(hand)

        function = glued
    return function

# Построение треугольника Паскаля и получение из него g
def pascalTriangle(functionVector):
    g, itog = '', []

    while len(functionVector) != 0:
        itog.append(functionVector)
        g += functionVector[0]
        replyFunction = ''

        for i in range(len(functionVector) - 1):
            replyFunction += ['0', '1'][functionVector[i] != functionVector[i + 1]]
        functionVector = replyFunction

    return ('\n'.join(itog), g)

# Полином Жегалкина по какому-либо g
def polinomJegalkina(g):
    polinom = []

    for loop, i in enumerate(['1', 'x3', 'x2', 'x2x3', 'x1', 'x1x3', 'x1x2', 'x1x2x3']):
        if int(g[loop]):
            polinom.append(i)

            if len(i) > 2: global L; L = '-'

    return ' ⊕ '.join(list(polinom))

# / / / / /

print(f'''
Совершенные формы:
 · СДНФ: { prettyFunction(SDNF) or 'Не существует...' }
 · СКНФ: { prettyFunction(SKNF, 1) or 'Не существует...' }

Минимизированные формы:
 · МДНФ: { (MDNF := prettyFunction(gluing(SDNF), False, True)) or 'Не существует...' }
 · МКНФ: { prettyFunction(gluing(SKNF), True, True) or 'Не существует...' }

Треугольник Паскаля:
{ (pascalTriangle := pascalTriangle(debugFunctionVector))[0] }

Полином Жегалкина (g = { pascalTriangle[1] }):
 · { polinomJegalkina(pascalTriangle[1]) or 'Не существует...' }

Принадлежность к классам:
 · T0: { T0 }
 · T1: { T1 }
 · S: { S }
 · L: { L }
 · M: { ['+', '-']['¬' in MDNF] }
''')