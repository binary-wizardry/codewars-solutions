# Get the Middle Character
# https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    return s[len(s) // 2 - 1 + len(s) % 2: len(s) // 2 + 1]
