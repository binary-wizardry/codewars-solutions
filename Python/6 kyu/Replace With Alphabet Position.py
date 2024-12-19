# Replace With Alphabet Position
# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    return ' '.join(str(ord(c) - ord('a') + 1) for c in text.lower() if c.isalpha())
