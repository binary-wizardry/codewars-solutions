# Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    return len([s for s in sentence if s in 'aeiou'])
