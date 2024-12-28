# Battleship field validator
# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

from itertools import groupby

def validate_battlefield(field):
    valid = {4: 1, 3: 2, 2: 3, 1: 24}  # scan twice: vertically and horizontally
    ships = {}
    for row in field:  # first scan
        for ship, group in groupby(row):
            if ship:
                cells = len(list(group))
                ships[cells] = ships.get(cells, 0) + 1
    field = [list(row) for row in zip(*field)]  # rotate field
    for row in field:  # second scan
        for ship, group in groupby(row):
            if ship:
                cells = len(list(group))
                ships[cells] = ships.get(cells, 0) + 1
    if ships != valid:  # checking ships count
        return False
# proximity check:
    field = [[0] * 10] + field + [[0] * 10]  # add empty boundaries
    field = [list(row) for row in zip(*field)]  # rotate field
    field = [[0] * 12] + field + [[0] * 12]  # add empty boundaries
    for i in range(1, 11):
        for j in range(1, 11):
            if field[i][j] and any([field[i-1][j-1], field[i-1][j+1], field[i+1][j+1], field[i+1][j-1]]):
                return False
    return True
