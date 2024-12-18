# Counting Duplicates
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

from collections import Counter

def duplicate_count(text):
    return sum(count > 1 for count in Counter(text.lower()).values())
