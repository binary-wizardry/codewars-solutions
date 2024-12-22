# Strings Mix
# https://www.codewars.com/kata/5629db57620258aa9d000014

from string import ascii_lowercase

def mix(s1, s2):
    counts = []
    for s in ascii_lowercase:
        a, b = s1.count(s), s2.count(s)
        count = max(a, b)
        if count > 1:
            source = '=' if a == b else ['1', '2'][a < b]
            counts.append(f'{source}:{s * count}')
    return '/'.join(sorted(sorted(counts), key=lambda x: len(x), reverse=True))
