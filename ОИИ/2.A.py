file = open('27A.txt')

# from random import shuffle
from math import dist

stars = [tuple(map(float, i.split())) for i in file]

clusters = [[], []]
centers = stars[56:58]

for _ in range(10):
    # ffdffdsfds
    for star in stars:
        minDist = 100
        numCluster = -1
        for i in range(len(centers)):
            targetDist = dist(star, centers[i])
            if targetDist < minDist:
                minDist, numCluster = targetDist, i
        clusters[numCluster].append(star)

    # gfdsgfsg
    for i in range(len(clusters)):
        cluster = clusters[i]

        sumdmin = 100000
        for j in cluster:
            tsumdmin = 0
            for k in cluster:
                tsumdmin += dist(j, k)

            if tsumdmin < sumdmin:
                sumdmin = tsumdmin
                centers[i] = j[0], j[1]

# / / / / /

# Распределение по кластерам
cluster1, cluster2 = [], []
for i in stars:
    x = i[0]

    if x < 4:
        cluster1.append(i)
    if x > 8:
        cluster2.append(i)

def centroid(cluster):
    minDistSum = 10 ** 100

    for i in range(len(cluster)):
        star1x, star1y = cluster[i]
        distSum = 0
        for j in range(i + 1, len(cluster)):
            star2x, star2y = cluster[j]

            distSum += dist(cluster[i], cluster[j])

            if distSum < minDistSum:
                minDistSum = distSum
                centroidX, centroidY = star1x, star1y

    return [centroidX, centroidY]

c1, c2 = centroid(cluster1), centroid(cluster2)

print(*centers, c1, c2, sep = '\n')

from cream import pogr
print('\n', pogr(centers[0], c1), pogr(centers[1], c2), sep = '\n')