#!/usr/bin/python3
def roman_to_int(roman_string):
    num_rom = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    temp, sum = 0, 0
    for c in roman_string:
        sum += num_rom[c] if num_rom[c] <= temp else num_rom[c] - temp * 2
        temp = num_rom[c]
    return sum
