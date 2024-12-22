# Strip Comments
# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def strip_comments(strng, markers):
    result = []
    for line in strng.split('\n'):
        for marker in markers:
            if marker in line:
                line = line[:line.index(marker)].rstrip()
        result.append(line)
    return '\n'.join(result)
