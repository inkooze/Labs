from random import randint
from package.activators import sigmoid, tanh, stupenka, softSign, softPlus, relu, leakyRelu, elu, softmax

x = tuple(randint(-99, 99) / 100 for _ in range(4))
w = tuple(randint(-99, 99) / 100 for _ in range(4))

layersNeuronsCount = 4, 2, 3, 2

for activator in [stupenka, softPlus, leakyRelu]:
	layersNeuronsValues = []

	for i in range(len(layersNeuronsCount)): # i = 0, 1, 2, 3
		layer = []
		for j in range(layersNeuronsCount[i]): # j = (0, 1, 2, 3), (0, 1), (0, 1, 2), (0, 1)
			if i == 0:
				layer.append(round(activator(x[j] * w[j]), 2))
			else:
				layer.append(round(activator(sum(layersNeuronsValues[i - 1][k] * randint(-99, 99) / 100 for k in range(layersNeuronsCount[i - 1]))), 2))

		layersNeuronsValues.append(layer)

	print(activator.__name__)
	for i in layersNeuronsValues:
		print(i)
	print()