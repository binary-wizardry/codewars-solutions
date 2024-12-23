# Twice linear
# https://www.codewars.com/kata/5672682212c8ecf83e000050

def dbl_linear(n):
    u = [1]
    index_y = index_z = 0
    for i in range(1, n + 1):
        y = 2 * u[index_y] + 1
        z = 3 * u[index_z] + 1
        u.append(min(y, z))
        if u[-1] == y:
            index_y += 1
        if u[-1] == z:
            index_z += 1
    return u[-1]
