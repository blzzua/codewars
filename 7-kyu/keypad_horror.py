# https://www.codewars.com/kata/5572392fee5b0180480001ae

def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('1234567890', '7894561230'))

