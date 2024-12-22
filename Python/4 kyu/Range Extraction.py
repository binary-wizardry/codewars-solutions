# Range Extraction
# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

import re

def solution(args):
    serials = [args[i] for i in range(1, len(args) - 1) if args[i + 1] - args[i -1] == 2]
    result = ','.join(map(str, args))
    for n in serials:
        result = result.replace(f',{n}', '#')
    return re.sub(r'#+,', '-', result)
