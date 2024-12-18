# Find The Parity Outlier
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    check = sum(x % 2 for x in integers[:3]) < 2
    for n in integers:
        if n % 2 == check:
            return n
