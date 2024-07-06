class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the values and their corresponding Roman numerals
        value_to_symbol = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        roman = []
        
        # Iterate over the values and symbols
        for value, symbol in value_to_symbol:
            while num >= value:
                num -= value
                roman.append(symbol)
        
        return ''.join(roman)
