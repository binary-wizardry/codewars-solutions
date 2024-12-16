# Mumbling
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(st):
    return '-'.join((s * n).title() for s, n in enumerate(st, 1))
