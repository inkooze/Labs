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
stars = [tuple(map(float, i.split())) for i in open('27a.txt')]

# shuffle(stars)
# centersMethod1 = stars[:2]
centersMethod1 = [(1.01142, 1.45567), (11.18348, 6.39232)]

## "Итеративное повторение шагов 3-5":
for _ in range(25):
    clustersMethod1 = [], []

    ### Распределение звёзд на основе их расстояния от центров кластеров в переменной centersMethod1:
    for star in stars:
        minToCenterDist = float('inf')

        for i in range(2):
            toCenterDist = dist(star, centersMethod1[i])

            if toCenterDist < minToCenterDist:
                minToCenterDist, nearClusterIndex = toCenterDist, i

        clustersMethod1[nearClusterIndex].append(star)

    ### "Шаг 5":
    for i in range(2):
        centersMethod1[i] = centroidCenterMass(clustersMethod1[i])

# Решение по центру масс:
clustersMethod2 = [], []

## Распределение звёзд по кластерам, на основе визуального представления:
for i in stars:
    x = i[0]

    if x < 4:
        clustersMethod2[0].append(i)
    if x > 8:
        clustersMethod2[1].append(i)

# Задание на защиту: найти самую дальнюю от центроида кластера (в каждом) звезду и вывести это расстояние
def maxDist(cluster, centroid):
    return max(dist(star, centroid) for star in cluster)

# Вывод по результатам подсчётов выше:
for i in range(2):
    firstCentr = centroidArithmeticMean(clustersMethod2[i])
    lastCentr = centersMethod1[i]

    print(f'Центроид: { firstCentr } -> { lastCentr }\nПогрешность: { ((firstCentr[0] - lastCentr[0]) ** 2 + (firstCentr[1] - lastCentr[1]) ** 2) ** 0.5 }\nТочек в кластере: { len(clustersMethod1[i]) } -> { len(clustersMethod2[i]) }\nРасстояние от самой дальней точки кластера: {maxDist(clustersMethod1[i], firstCentr)} -> {maxDist(clustersMethod2[i], lastCentr)}\n')