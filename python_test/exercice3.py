import numpy as np

digits = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

dict2roman = {
    1 : "I",
    4 : "IV",
    5 : "V",
    9 : "IX",
    10 : "X",
    40 : "XL",
    50 : "L",
    90 : "XC",
    100 : "C",
    400 : "CD",
    500 : "D",
    900 : "CM",
    1000 : "M"
}

sorted_keys = list(dict2roman.keys())
sorted_keys.reverse()

def int2roman(integer, starting_index = 0):
    roman = ""
    highest_key = sorted_keys[starting_index]

    while highest_key > integer:
        starting_index += 1
        highest_key = sorted_keys[starting_index]
    
    quotient = integer // highest_key
    reminder = integer % highest_key
    
    roman += quotient * dict2roman[highest_key]
    if reminder > 0:
        roman += int2roman(reminder, starting_index + 1)

    return roman

print(f"8 should be VIII, and is {int2roman(8)}")
print(f"10 should be X, and is {int2roman(10)}")
print(f"67 should be LXVII, and is {int2roman(67)}")
print(f"800 should be DCCC, and is {int2roman(800)}")
print(f"3999 should be MMMCMXCIX, and is {int2roman(3999)}")