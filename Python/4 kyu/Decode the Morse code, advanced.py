# Decode the Morse code, advanced
# https://www.codewars.com/kata/54b72c16cd7f5154e9000457

from itertools import groupby

def decode_bits(bits):
    bits, morse_code = bits.strip('0'), ''
    pattern = {'111': '-', '1': '.', '0' * 7: ' ', '000': '#', '0': ''}
    time_unit = min(len(list(group)) for _, group in groupby(bits))
    pattern = {k * time_unit: v for k, v in pattern.items()}
    while bits:
        for code, symbol in pattern.items():
            while bits.startswith(code):
                morse_code += symbol
                bits = bits[len(code):]
    return morse_code

def decode_morse(morseCode):
    morseCode = [seq.split('#') for seq in morseCode.split()]
    return ' '.join(''.join(MORSE_CODE[symbol] for symbol in word) for word in morseCode)
