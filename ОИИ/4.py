from math import exp
from pandas import ExcelWriter
from package.excel import addChart
from package.graphics import triangleFunction, trapezoidFunction, gaussFunction

# сигма на лекции была 400, можно брать 10-500

clusters = [], [], []
for x in range(100, 300 + 1):
    clusters[0].append((x, round(triangleFunction(180, 240, 300, x), 2)))
    clusters[1].append((x, round(trapezoidFunction(160, 180, 200, 270, x), 2)))
    clusters[2].append((x, gaussFunction(130, 15, x)))

# Автообновление диаграммы
with ExcelWriter('4 (Функции принадлежностей, прямые графики).xlsx', engine = 'xlsxwriter') as file:
    lastChartLine = addChart(file, [i[0] for i in clusters[0]], [i[1] for i in clusters[0]], 0, 'line')
    lastChartLine = addChart(file, [i[0] for i in clusters[1]], [i[1] for i in clusters[1]], lastChartLine, 'line')
    addChart(file, [i[0] for i in clusters[2]], [i[1] for i in clusters[2]], lastChartLine, 'line')

print('Графики функций добавлены в файл\n')


method1, method2 = 0, 0
print('Дефаззификация функций двумя методами:')
for cluster in clusters:
    E1 = sum(x * f for x, f in cluster)
    E2 = sum(f for x, f in cluster)

    print('-', round(E1 / E2, 2), end = ', ')
    method1 += round(E1 / E2, 2)

    for i in range(len(cluster)):
        if sum(j[0] for j in cluster[:i + 1]) > 0.5 * sum(j[0] for j in cluster[i + 2:]):
            print(cluster[i][0])
            method2 += cluster[i][0]
            break

print(f'''\nУсреднённые значения
- Первого метода = {method1 / 3:.2f}
- Второго метода = {method2 / 3:.2f}''')