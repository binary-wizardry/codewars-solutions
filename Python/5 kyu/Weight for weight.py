# Weight for weight
# https://www.codewars.com/kata/55c6126177c9441a570000cc

def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda s: (sum(int(n) for n in s), s)))
