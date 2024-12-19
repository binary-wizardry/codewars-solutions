# Tribonacci Sequence
# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]
