# Moving Zeros To The End
# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    return [n for n in lst if n] + [n for n in lst if not n]
