from collections import OrderedDict
# https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals
import sys
# Dr.Babb's code


def number_conversion(number):

    conversion_dictionary = {
        1000: "M",
        900: "DM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def roman_numeral(number):
        for n in conversion_dictionary.keys():
            x, y = divmod(number, n)
            yield conversion_dictionary[n] * x
            number -= (n * x)
            if number <= 0:
                break

    return "".join([a for a in roman_numeral(number)])
    # https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals


def main() -> int:
    """Echo the input arguments to standard output"""
    entered = input("enter a decimal number: ")
    print(number_conversion(int(entered)))
    return 0
    # Dr. Babb's code


if __name__ == '__main__':
    sys.exit(main())
    # Dr. Babb's code
