# You're a square!
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e

from math import sqrt

def is_square(n):    
    return int(sqrt(n)) == sqrt(n) if n >= 0 else False
