from math import exp, log

# / / /

def sigmoid(x):
    return 1 / (1 + exp(-x))

def tanh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

def stupenka(x):
    return 0 if x < 0 else 1

def softSign(x):
    return x / (1 + abs(x))

def softPlus(x):
    return log(1 + exp(x))

def relu(x):
    return 0 if x < 0 else x

def leakyRelu(x, a = 0.01):
    return a * x if x < 0 else x

def elu(x, a = 1.0):
    return a * (exp(x) - 1) if x < 0 else x

# Функция активации для списка значений (c - константа для численной стабильности, обычно -max(xList))
def softmax(xList, c = 0):
    expList = [exp(x + c) for x in xList]
    expSum = sum(expList)
    return [ev / sum(expList) for ev in expList]