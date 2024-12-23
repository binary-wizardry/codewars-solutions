# Pyramid Slide Down
# https://www.codewars.com/kata/551f23362ff852e2ab000037

def longest_slide_down(pyramid):
    for floor in range(len(pyramid) - 1, 0, -1):
        for index, num in enumerate(pyramid[floor - 1]):
            pyramid[floor - 1][index] += max(pyramid[floor][index], pyramid[floor][index + 1])
    return pyramid[0][0]
