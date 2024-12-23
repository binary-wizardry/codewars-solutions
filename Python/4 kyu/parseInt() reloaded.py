# parseInt() reloaded
# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5

def parse_before_100(string):
    numbers = {'ninety': 90, 'eighty': 80, 'seventy': 70, 'sixty': 60, 'fifty': 50,
               'forty': 40, 'thirty': 30, 'twenty': 20,
               'nineteen': 19, 'eighteen': 18, 'seventeen': 17, 'sixteen': 16, 'fifteen': 15,
               'fourteen': 14, 'thirteen': 13, 'twelve': 12, 'eleven': 11, 'ten': 10,
               'nine': 9, 'eight': 8, 'seven': 7, 'six': 6, 'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
    number = 0
    for key, value in numbers.items():
        if key in string:
            number += value
            string = string.replace(key, '', 1)
    return number


def parse_before_1000(string):
    if 'hundred' in string:
        hundred, string = string.split('hundred')
    else:
        hundred = ''
    return parse_before_100(hundred) * 100 + parse_before_100(string)


def parse_int(string):
    if 'million' in string:
        million, string = string.split('million')
    else:
        million = ''
    if 'thousand' in string:
        thousand, string = string.split('thousand')
    else:
        thousand = ''
    return parse_before_1000(million) * 1000000 + parse_before_1000(thousand) * 1000 + parse_before_1000(string)
