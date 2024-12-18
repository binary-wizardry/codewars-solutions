# Sum of Digits / Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):  # recursion
    return n if n < 10 else digital_root(sum(map(int, str(n))))

def digital_root(n):  # maths
    return n % 9 or 9 if n else 0
