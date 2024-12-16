# Highest and Lowest
# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    numbers = str(max(int(n) for n in numbers.split())) + ' ' + str(min(int(n) for n in numbers.split()))
    return numbers
