# Sum Strings as Numbers
# https://www.codewars.com/kata/5324945e2ece5e1f32000370

def sum_strings(x, y):
    length = max(len(x), len(y))
    x = x.rjust(length, '0')
    y = y.rjust(length, '0')
    stack = 0
    result = ''
    for i in range(length - 1, -1, -1):
        summa = int(x[i]) + int(y[i]) + stack
        stack = summa // 10
        result += f'{summa % 10}'
    result += f'{stack}'
    result = result[::-1].lstrip('0')
    return result if result else '0'
