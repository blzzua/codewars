# https://www.codewars.com/kata/599b4e682b862b8498000021
import sys

# This list should contain all Unicode characters that are digits but not decimals
digits_not_decimals = [] # Your code here

# This list should contain all Unicode characters that are numeric but not digits
numeric_not_digits = [] # Your code here


for i in range(sys.maxunicode + 1):
    char = chr(i)
    if char.isdigit() and not char.isdecimal():
        digits_not_decimals.append(char)
    if char.isnumeric() and not char.isdigit():
        numeric_not_digits.append(char)
