# Sudoku Solver
# https://www.codewars.com/kata/5296bc77afba8baa690002d7

def checker(i, j, puzzle) -> int:
    """return digit for the i, j cell if can be defined or 0"""
    digits = set(range(1, 9 + 1))
    row = set(puzzle[i])
    col = set(row[j] for row in puzzle)
    i, j = i // 3 * 3, j // 3 * 3
    square = set(puzzle[row][col] for row in range(i, i + 3) for col in range(j, j + 3))
    number = digits - row - col - square
    return number.pop() if len(number) == 1 else 0


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    while not all(all(row) for row in puzzle):
        for i in range(9):
            for j in range(9):
                if not puzzle[i][j]:
                    puzzle[i][j] = checker(i, j, puzzle)
    return puzzle
