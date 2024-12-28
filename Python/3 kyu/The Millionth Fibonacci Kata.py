# The Millionth Fibonacci Kata
# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26

def calc(n):
    """Function from Exercise 1.19 in:
https://web.archive.org/web/20220614001843/https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4
    """
    if n == 0:
        return (0, 1)
    elif n == 1:
        return (1, 1)
    else:
        a, b = calc(n // 2)
        p = a * (2 * b - a)
        q = b * b + a * a
        return (p, q) if n % 2 == 0 else (q, p + q)

def fib(n):
    """Calculates the nth Fibonacci number"""
    if n >= 0:
        return calc(n)[0]
    else:
        return -calc(-n)[0] if n % 2 ==0 else calc(-n)[0]
