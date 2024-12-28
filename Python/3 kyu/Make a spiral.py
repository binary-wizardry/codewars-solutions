# Make a spiral
# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

def spiralize(size):
    if size == 3:
        return [[1, 1, 1], [0, 0, 1], [1, 1, 1]]
    if size == 2:
        return [[1, 1], [0, 1]]
    spiral = spiralize(size - 2)  # recursion
    spiral = [list(row[::-1]) for row in zip(*spiral)]  # rotate 90 clockwise
    spiral = [[1] * (size - 2), [0] * (size - 3) + [1]] + spiral # add 2 lines
    spiral = [list(row[::-1]) for row in zip(*spiral)]  # rotate 90 clockwise again
    spiral = [[1] * size, [0] * (size - 1) + [1]] + spiral  # add 2 lines again
    return spiral
