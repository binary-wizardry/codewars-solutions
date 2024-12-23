# Sum by Factors
# https://www.codewars.com/kata/54d496788776e49e6b00052f

def prime_factors(n):
    factor = 2
    factors = set()
    n = abs(n)
    while n > 1:
        if n % factor:
            factor += 1
        else:
            factors.add(factor)
            n //= factor
    return factors

def sum_for_list(lst): 
    factors = set()
    for n in lst:
        factors.update(prime_factors(n))
    factors = sorted(factors)
    return [[p, sum(n for n in lst if not n % p)] for p in factors]
