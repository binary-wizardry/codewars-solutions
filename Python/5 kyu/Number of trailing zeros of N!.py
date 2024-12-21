# Number of trailing zeros of N!
# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

def zeros(n):
    x = 5
    result = len(range(x, n + 1, x))
    while n > x:
        x *= 5
        result += len(range(x, n + 1, x))
    return result
