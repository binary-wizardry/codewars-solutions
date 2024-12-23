# Recover a secret string from random triplets
# https://www.codewars.com/kata/53f40dff5f9d31b813000774
# triplets is a list of triplets from the secret string. Return the string.

def check(seq, a, b):
    if seq.index(a) > seq.index(b):
        seq.remove(a)
        seq.insert(seq.index(b), a)

def recover_secret(triplets):
    letters = list(set(sum(triplets, [])))
    for triplet in triplets:
        check(letters, triplet[0], triplet[1])
        check(letters, triplet[1], triplet[2])
    for triplet in triplets:
        check(letters, triplet[1], triplet[2])
        check(letters, triplet[0], triplet[1])
    return ''.join(letters)
