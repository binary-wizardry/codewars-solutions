# Duplicate Encoder
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    return ''.join('(' if word.lower().count(c) == 1 else ')' for c in word.lower())
