# Human Readable Time
# https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    return f'{seconds // 3600:02}:{seconds % 3600 // 60:02}:{seconds % 60:02}'
