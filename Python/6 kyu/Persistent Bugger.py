# Persistent Bugger
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

from functools import reduce
from operator import mul

def persistence(n):
    return 0 if n < 10 else persistence(reduce(mul, map(int, str(n)))) + 1
