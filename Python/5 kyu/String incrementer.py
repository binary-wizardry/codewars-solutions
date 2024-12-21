# String incrementer
# https://www.codewars.com/kata/54a91a4883a7de5d7800009c

import re

def increment_string(strng):
    match = re.search(r'\d+$', strng) or '0'
    number, format = int(match[0]), len(match[0])
    return strng.rstrip('0123456789') + f'{number + 1}'.rjust(format, '0')
