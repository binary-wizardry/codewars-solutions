# Primes in numbers
# https://www.codewars.com/kata/54d512e62a5e54c96200019e

def prime_factors(n):
    divider = 2
    result = ''
    while n != 1:
        pow = 0
        while n % divider == 0:
            n //= divider
            pow += 1
        if not pow: 
            pass
        elif pow == 1:
            result += f'({divider})'
        else:
            result += f'({divider}**{pow})'
        divider +=1
    return result
