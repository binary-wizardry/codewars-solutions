# Roman Numerals Helper
# https://www.codewars.com/kata/51b66044bce5799a7f000003

class RomanNumerals:
    table = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
             'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
             'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    
    @staticmethod
    def to_roman(val : int) -> str:
        roman = ''
        while val:
            for symbol, value in RomanNumerals.table.items():
                while val >= value:
                    val -= value
                    roman += symbol
        return roman

    @staticmethod
    def from_roman(roman_num : str) -> int:
        number = 0
        for symbol, value in RomanNumerals.table.items():
            while roman_num.startswith(symbol):
                number += value
                roman_num = roman_num[len(symbol):]
        return number
