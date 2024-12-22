# The observed PIN
# https://www.codewars.com/kata/5263c6999e0f40dee200059d

from itertools import product

def get_pins(observed):
    pattern = {'1': '124', '2': '1235', '3': '236', '4': '1457', '5': '24568',
               '6': '3569', '7': '478', '8': '57890', '9': '689', '0': '80'}
    possible = [pattern[n] for n in observed]
    return [''.join(combo) for combo in product(*possible)]
