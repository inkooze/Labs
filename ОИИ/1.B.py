from math import dist

stars = [tuple(map(float, i.replace(',', '.').split())) for i in open('27B.txt')]

# Распределение по кластерам
cluster1, cluster2, cluster3, cluster4, cluster5 = [], [], [], [], []
for i in stars:
    x, y = i[0], i[1]

    if x < -15 and y < 5:
        cluster1.append(i)
    if x < -5 and y > 5:
        cluster2.append(i)
    if -5 < x < 5 and -5 < y < 5:
        cluster3.append(i)
    if x > 5 and y > 5:
        cluster4.append(i)
    if x > 5 and y < -5:
        cluster5.append(i)

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

# centroid1 = centroid(cluster1)
# centroid2 = centroid(cluster2)
# centroid3 = centroid(cluster3)
# centroid4 = centroid(cluster4)
# centroid5 = centroid(cluster5)
#
# allCentroidX = (centroid1[0] + centroid2[0] + centroid3[0] + centroid4[0] + centroid5[0]) / 5
# allCentroidY = (centroid1[1] + centroid2[1] + centroid3[1] + centroid4[1] + centroid5[1]) / 5
#
# print(allCentroidX, allCentroidY)
#
# print(centroid1, centroid2, centroid3, centroid4, centroid5)
#
# print(dist(centroid1, [allCentroidX, allCentroidY]))
# print(dist(centroid2, [allCentroidX, allCentroidY]))
# print(dist(centroid3, [allCentroidX, allCentroidY]))
# print(dist(centroid4, [allCentroidX, allCentroidY]))
# print(dist(centroid5, [allCentroidX, allCentroidY]))
#
# print(centroid(stars))

print(len(cluster3), len(cluster1))