# Scramblies
# https://www.codewars.com/kata/55c04b4cc56a697bb0000048

def scramble(s1, s2):
    return all(s1.count(s) >= s2.count(s) for s in set(s2))
