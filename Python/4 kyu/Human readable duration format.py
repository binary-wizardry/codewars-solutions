# Human readable duration format
# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    minutes, seconds = seconds // 60, seconds % 60
    hours, minutes = minutes // 60, minutes % 60
    days, hours = hours // 24, hours % 24
    years, days = days // 365, days % 365
    result = {'year': years, 'day': days, 'hour': hours, 'minute': minutes, 'second': seconds}
    result = ', '.join(f'{v} {k + "s" if v > 1 else k}' for k, v in result.items() if v)
    result = result[::-1].replace(' ,', ' dna ', 1)[::-1]
    return result if result else 'now'
