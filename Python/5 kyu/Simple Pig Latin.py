# Simple Pig Latin
# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    return ' '.join(w[1:] + w[0] + 'ay' if w.isalpha() else w for w in text.split())
