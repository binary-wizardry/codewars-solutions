# Multiples of 3 or 5
# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    return sum(n for n in range(number) if  not n % 3 or not n % 5)
