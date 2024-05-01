# https://www.codewars.com/kata/61ce25e92ca4fb000f689fb0

def isbn_converter(isbn):
    i13 = '978' + isbn[:-1].replace('-','')
    checksum = sum(int(digit)*3 if i % 2 else int(digit) for i, digit in enumerate(i13)) % 10
    if checksum:
        checksum = 10 - checksum
    return '978-' + isbn[:-1] + str(checksum)
