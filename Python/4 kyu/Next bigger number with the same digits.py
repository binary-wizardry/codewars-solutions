# Next bigger number with the same digits
# https://www.codewars.com/kata/55983863da40caa2c900004e

def next_bigger(n):
    n = list(str(n))
    for index in range(len(n) - 1, 0, -1):
        if n[index - 1] < n[index]:
            boundary = n[index - 1]
            rest = sorted(n[index - 1:])
            number = [x for x in rest if x > boundary][0]
            rest.remove(number)
            return int(''.join(n[:index - 1] + [number] + rest))
    return -1
