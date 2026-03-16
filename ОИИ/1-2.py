# Общие объявления:
from math import dist
from statistics import mean
from random import shuffle

# / / / / /

## Центроид, как центр масс звёзд, рассматриваемых в кластере:
def centroidCenterMass(cluster):
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

# Задание на защиту: найти самую дальнюю от центроида кластера (в каждом) звезду и вывести это расстояние
def maxDist(cluster, centroid):
    return max(dist(star, centroid) for star in cluster)

# / / / / /

k = int(input('Введи k... '))
stars = [tuple(map(float, i.split())) for i in open(f'1-2{'a' if k == 2 else 'b'}.txt')]

# Решение по центру масс:
## Распределение звёзд по кластерам, на основе визуального представления:
clustersMethod1 = tuple([] for _ in range(k))
for i in stars:
    X, Y = i[0], i[1]

    if k == 2:
        if X < 4:
            clustersMethod1[0].append(i)
        if X > 8:
            clustersMethod1[1].append(i)
    else:
        if Y > 7:
            if X < 0:
                clustersMethod1[0].append(i)
            else:
                clustersMethod1[1].append(i)
        else:
            if X < -15:
                clustersMethod1[2].append(i)
            elif X > 5:
                clustersMethod1[3].append(i)
            else:
                clustersMethod1[4].append(i)


# Решение через k-means:
iterations = int(input('Введи количество итераций... '))

shuffle(stars)
centersMethod2 = stars[:k]
# centersMethod2 = [(1.01142, 1.45567), (11.18348, 6.39232)] # [(-17.30774, 18.39937), (19.11043, 18.35931), (-29.66172, -10.89271), (19.58036, -17.80037), (-0.01541, 0.01946)] для файла b

## "Итеративное повторение шагов 3-5":
for _ in range(iterations):
    clustersMethod2 = tuple([] for _ in range(k))

    ### Распределение звёзд на основе их расстояния от центров кластеров в переменной centersMethod2:
    for star in stars:
        minToCenterDist = float('inf')

        for i in range(k):
            toCenterDist = dist(star, centersMethod2[i])

            if toCenterDist < minToCenterDist:
                minToCenterDist, nearClusterIndex = toCenterDist, i

        clustersMethod2[nearClusterIndex].append(star)

    ### "Шаг 5":
    for i in range(k):
        centersMethod2[i] = centroidCenterMass(clustersMethod2[i])

# Вывод по результатам подсчётов выше:
for i in range(k):
    firstCentr = centroidArithmeticMean(clustersMethod1[i])
    lastCentr = centersMethod2[i]

    print(f'\nЦентроид: { firstCentr } -> { lastCentr }\nПогрешность: { ((firstCentr[0] - lastCentr[0]) ** 2 + (firstCentr[1] - lastCentr[1]) ** 2) ** 0.5 }\nТочек в кластере: { len(clustersMethod1[i]) } -> { len(clustersMethod2[i]) }\nРасстояние от самой дальней точки кластера: {maxDist(clustersMethod1[i], firstCentr)} -> {maxDist(clustersMethod2[i], lastCentr)}')