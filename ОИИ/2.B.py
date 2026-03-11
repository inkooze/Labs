# Общие объявления:
from math import dist
from statistics import mean
from random import shuffle

## Центроид, как центр масс звёзд, рассматриваемых в кластере:
def centroidCenterMass(cluster: list[tuple]):
    minSumDist = float('inf')

    for handStar in cluster:
        sumDist = 0

        for fingerStar in cluster:
            sumDist += dist(handStar, fingerStar)

            if sumDist < minSumDist:
                minSumDist = sumDist
                X, Y = handStar

    return X, Y

# Центроид, как среднее арифметическое соответствующих координат всех звёзд кластера:
def centroidArithmeticMean(cluster):
    X = mean(star[0] for star in cluster)
    Y = mean(star[1] for star in cluster)

    return X, Y

# Решение через k-means:
stars = [tuple(map(float, i.split())) for i in open('27B.txt')]

# shuffle(stars)
# centersMethod1 = stars[:5]
centersMethod1 = [(-17.30774, 18.39937), (19.11043, 18.35931), (-29.66172, -10.89271), (19.58036, -17.80037), (-0.01541, 0.01946)]

## "Итеративное повторение шагов 3-5":
for _ in range(10):
    clustersMethod1 = [], [], [], [], []

    ### Распределение звёзд на основе их расстояния от центров кластеров в переменной centersMethod1:
    for star in stars:
        minToCenterDist = float('inf')

        for i in range(5):
            toCenterDist = dist(star, centersMethod1[i])

            if toCenterDist < minToCenterDist:
                minToCenterDist, nearClusterIndex = toCenterDist, i

        clustersMethod1[nearClusterIndex].append(star)

    ### "Шаг 5":
    for i in range(5):
        centersMethod1[i] = centroidCenterMass(clustersMethod1[i])

# Решение по центру масс:
clustersMethod2 = [], [], [], [], []

## Распределение звёзд по кластерам, на основе визуального представления:
for i in stars:
    X, Y = i[0], i[1]

    if Y > 7:
        if X < 0:
            clustersMethod2[0].append(i)
        else:
            clustersMethod2[1].append(i)
    else:
        if X < -15:
            clustersMethod2[2].append(i)
        elif X > 5:
            clustersMethod2[3].append(i)
        else:
            clustersMethod2[4].append(i)

# Вывод по результатам подсчётов выше:
for i in range(5):
    firstCentr = centroidArithmeticMean(clustersMethod2[i])
    lastCentr = centersMethod1[i]

    print(f'{ i + 1 }. { firstCentr } -> { lastCentr } | Погрешность = { ((firstCentr[0] - lastCentr[0]) ** 2 + (firstCentr[1] - lastCentr[1]) ** 2) ** 0.5 } | Точек в кластере: { len(clustersMethod1[i]) } -> { len(clustersMethod2[i]) }')