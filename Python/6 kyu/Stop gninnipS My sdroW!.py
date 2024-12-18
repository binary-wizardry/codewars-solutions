# Stop gninnipS My sdroW!
# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    return ' '.join(s if len(s) < 5 else s[::-1] for s in sentence.split())
