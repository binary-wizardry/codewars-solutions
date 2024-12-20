# Directions Reduction
# https://www.codewars.com/kata/550f22f4d758534c1100025a

def dir_reduc(arr):
    def check(arr):
        for f in flags:
            if f in arr:
                return f
    flags = 'NORTH SOUTH', 'SOUTH NORTH', 'EAST WEST', 'WEST EAST'
    arr = ' '.join(arr)
    while flag := check(arr):
        arr = ' '.join(arr.replace(flag, '').split())
    return arr.split()
