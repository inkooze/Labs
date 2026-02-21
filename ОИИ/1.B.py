from math import dist

stars = [tuple(map(float, i.replace(',', '.').split())) for i in open('27B.txt')]

# Распределение по кластерам
cluster1, cluster2, cluster3, cluster4, cluster5 = [], [], [], [], []
for i in stars:
    x, y = i[0], i[1]


    if y > 7:
        if x < 0:
            cluster1.append(i)
        else:
            cluster2.append(i)
    else:
        if x < -15:
            cluster3.append(i)
        elif x > 5:
            cluster4.append(i)
        else:
            cluster5.append(i)

    # if x < -15 and y < 5:
    #     cluster1.append(i)
    # elif x < -5 and y > 5:
    #     cluster2.append(i)
    # elif x > 5 and y > 5:
    #     cluster4.append(i)
    # elif x > 5 and y < -5:
    #     cluster5.append(i)
    # else:
    #     cluster3.append(i)

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

    return centroidX, centroidY

def arifmCentroid(cluster):
    xsum, ysum = 0, 0

    for i in cluster:
        xsum += i[0]
        ysum += i[1]

    return xsum / len(cluster), ysum / len(cluster)

centroid1 = centroid(cluster1)
centroid2 = centroid(cluster2)
centroid3 = centroid(cluster3)
centroid4 = centroid(cluster4)
centroid5 = centroid(cluster5)
print(centroid1, centroid2, centroid3, centroid4, centroid5, sep = '\n')

allCentroidX = (centroid1[0] + centroid2[0] + centroid3[0] + centroid4[0] + centroid5[0]) / 5
allCentroidY = (centroid1[1] + centroid2[1] + centroid3[1] + centroid4[1] + centroid5[1]) / 5
print('\nЦентр системы кластеров: ', allCentroidX, allCentroidY, '\n')

print(dist(centroid1, [allCentroidX, allCentroidY]))
print(dist(centroid2, [allCentroidX, allCentroidY]))
print(dist(centroid3, [allCentroidX, allCentroidY]))
print(dist(centroid4, [allCentroidX, allCentroidY]))
print(dist(centroid5, [allCentroidX, allCentroidY]))

print('\n...\n')

print(len(cluster5), len(cluster4))

print('\n......\n')

centroid1 = arifmCentroid(cluster1)
centroid2 = arifmCentroid(cluster2)
centroid3 = arifmCentroid(cluster3)
centroid4 = arifmCentroid(cluster4)
centroid5 = arifmCentroid(cluster5)
print(centroid1, centroid2, centroid3, centroid4, centroid5, sep = '\n')

allCentroidX = (centroid1[0] + centroid2[0] + centroid3[0] + centroid4[0] + centroid5[0]) / 5
allCentroidY = (centroid1[1] + centroid2[1] + centroid3[1] + centroid4[1] + centroid5[1]) / 5
print('\nЦентр системы кластеров: ', allCentroidX, allCentroidY, '\n')

print(dist(centroid1, [allCentroidX, allCentroidY]))
print(dist(centroid2, [allCentroidX, allCentroidY]))
print(dist(centroid3, [allCentroidX, allCentroidY]))
print(dist(centroid4, [allCentroidX, allCentroidY]))
print(dist(centroid5, [allCentroidX, allCentroidY]))

print('\n...\n')

print(len(cluster5), len(cluster3))