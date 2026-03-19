from functools import reduce

# / / /

# Вычисление степеней принадлежности
def accessoryDegrees(objects: dict[str, set], strict: set) -> list:
    return dict(sorted(((objName, len(objAttrs & strict) / len(objAttrs | strict)) for objName, objAttrs in objects.items()), key = lambda el: el[1], reverse = True))

# Создание матрицы Саати и вычисление на её основе функций принадлежности
def accessoryFunction(l: int, marks: list) -> tuple[list[list], list]:
    marks = iter(marks)
    matrix = [[1] * l for _ in range(l)]
    for i in range(l - 1):
        for j in range(i + 1, l):
            matrix[i][j] = next(marks)
            matrix[j][i] = round(1 / matrix[i][j], 2)

    wAll = [reduce(lambda a, b: a * b, row) ** (1 / len(row)) for row in matrix]
    wNormalized = [round(w / sum(wAll), 3) for w in wAll]

    return matrix, wNormalized

def dictionaryOutput(dictionary: dict) -> str:
    return'\n'.join(f"- {k}: {v}" for k, v in dictionary.items())

def matrixOutput(matrix: list[list[float]]) -> str:
    rows = []
    for row in matrix:
        rows.append(''.join(str(i).ljust(8) for i in row))
    return '\n'.join(rows)