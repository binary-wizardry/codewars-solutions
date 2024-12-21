# Perimeter of squares in a rectangle
# https://www.codewars.com/kata/559a28007caad2ac4e000083

def perimeter(n):
    fib = [1, 1]
    while len(fib) < n + 1:
        fib.append(fib[-2] + fib[-1])
    return 4 * sum(fib[:n + 1])
