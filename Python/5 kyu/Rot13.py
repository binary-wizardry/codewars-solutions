# Rot13
# https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    return ''.join(chr((ord(c) + 13 - (shift := ord('a') if c.islower() else ord('A'))) % 26 + shift) if c.isalpha() else c for c in message)
