# Isograms
# https://www.codewars.com/kata/54ba84be607a92aa900000f1

def is_isogram(string):
    return len(set(string.lower())) == len(string)
