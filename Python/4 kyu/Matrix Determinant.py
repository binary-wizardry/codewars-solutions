# Matrix Determinant
# https://www.codewars.com/kata/52a382ee44408cea2500074c

def minor(matrix, index):
    return [row[:index] + row[index + 1:] for row in matrix[1:]]

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return sum((-1) ** i * a * determinant(minor(matrix, i)) for i, a in enumerate(matrix[0]))
