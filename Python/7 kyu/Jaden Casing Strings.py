# Jaden Casing Strings
# https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string):
    return ' '.join(map(str.capitalize, string.split()))
