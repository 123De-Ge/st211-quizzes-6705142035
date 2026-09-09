class RomanNumerals:

    def __init__(self):
        self.roman_values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

    def to_roman(self, number):

        if not isinstance(number, int):
            raise TypeError("Number must be an integer.")

        if number <= 0:
            raise ValueError("Number must be greater than 0.")

        roman_numeral = ""

        for value, symbol in self.roman_values:

            while number >= value:
                roman_numeral += symbol
                number -= value

        return roman_numeral