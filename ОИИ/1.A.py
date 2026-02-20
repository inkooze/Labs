from math import dist

stars = [tuple(map(float, i.split())) for i in open('27A.txt')]

# Распределение по кластерам
cluster1, cluster2 = [], []
for i in stars:
    x = i[0]

    if x < 4:
        cluster1.append(i)
    if x > 8:
        cluster2.append(i)

def centroid(cluster):
    minDist, maxDist, minDistSum = 10 ** 10, -10 ** 10, 10 ** 10

    for i in range(len(cluster)):
        star1x, star1y = cluster[i]
        distSum = 0
        for j in range(i + 1, len(cluster)):
            star2x, star2y = cluster[j]

            distTemp = dist(cluster[i], cluster[j])
            distSum += distTemp

            if distSum < minDistSum:
                minDistSum = distSum
                centroidX, centroidY = star1x, star1y

            if distTemp > maxDist:
                maxDist = distTemp
            if distTemp < minDist:
                minDist = distTemp

    return centroidX, centroidY, minDist, maxDist

print(int(centroid(cluster1)[3] * 100000), int(centroid(cluster2)[2] * 100000))