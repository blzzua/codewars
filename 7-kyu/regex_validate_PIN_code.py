# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

# regex is nessesary.
import re

# clever but used python re.fullmatch to avoid false match of '1234\n'
def validate_pin(pin):
    return bool(re.fullmatch("\d{4}|\d{6}", pin))

# clever: used \Z to avoid false match of '1234\n'
def validate_pin(pin):
    return re.match(r'(?:\d{4}|\d{6})\Z', pin) is not None

#  my solution. used negative lookahead to avoid false match of '1234\n'
def validate_pin(pin):
    return bool(re.match(r'^(\d{4}|\d{6})(?!\n)$', pin))
