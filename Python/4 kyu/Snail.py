# Snail
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

from itertools import cycle, chain, tee

def snail(snail_map):
    result = []
    n = len(snail_map[0])
    directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    steps = chain([n - 1], *zip(*tee(range(n - 1, 0, -1), 2)), [bool(n)])
    i, j = 0, 0
    for (delta_i, delta_j), step in zip(directions, steps):
        for _ in range(step):
            result.append(snail_map[i][j])
            i += delta_i
            j += delta_j
    return result    
