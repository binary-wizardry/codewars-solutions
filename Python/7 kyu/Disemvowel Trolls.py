# Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    return ''.join(s for s in string_ if s not in 'aeiuoAEIUO')
