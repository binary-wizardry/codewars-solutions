# Find the odd int
# https://www.codewars.com/kata/54da5a58ea159efa38000836

from collections import Counter

def find_it(seq):
    for key, value in Counter(seq).items():
        if value % 2:
            return key
