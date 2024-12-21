# Product of consecutive Fib numbers
# https://www.codewars.com/kata/5541f58a944b85ce6d00006a

def product_fib(_prod):
    a, b = 0, 1
    while a * b < _prod:
        a, b = b, a + b
    return [a, b, a * b == _prod]
