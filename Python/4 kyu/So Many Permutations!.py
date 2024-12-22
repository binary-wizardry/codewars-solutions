# So Many Permutations!
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

from itertools import permutations as prmt

def permutations(s):
    return [''.join(combo) for combo in set(prmt(s))]
