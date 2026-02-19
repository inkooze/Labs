'''
Работа №10 - Вариант 16 - Матрицы (двумерные массивы данных)
- Определить и поменять местами максимальное и минимальное значения двух квадратных матриц.
'''''

matrix1 = [
  [1, 2],
  [3, 4]
]

matrix2 = [
  [4, 3],
  [2, 1]
]

# Поиск максимума/минимума в матрице
# minMaxFlag - True поиск максимума, False - минимума
def matrixExtr(matrix: list[list], minMaxFlag: bool = False) -> tuple:
  extVal, extValI, extValJ = matrix[0][0], 0, 0

  for i, row in enumerate(matrix):
    for j, el in enumerate(row):
      if (minMaxFlag and el > extVal) or (not minMaxFlag and el < extVal):
        extVal, extValI, extValJ = el, i, j

  return extVal, extValI, extValJ

maxVal, maxValI, maxValJ = matrixExtr(matrix1, True)
minVal, minValI, minValJ = matrixExtr(matrix2)

matrix1[maxValI][maxValJ], matrix2[minValI][minValJ] = minVal, maxVal

print(f'''- Максимальный элемент в первой матрице на строке { maxValI + 1 }, столбце { maxValJ + 1 } = { maxVal }
- Минимальный элемент во второй матрице на строке { minValI + 1 }, столбце { minValJ + 1 } = { minVal }

Матрицы после перестановки максимального и минимального элементов местами:
- Первая матрица: { matrix1 }
- Вторая матрица: { matrix2 }''')