# https://www.codewars.com/kata/52f3149496de55aded000410

def sum_digits(number):
    return sum(int(d) for d in str(number) if d.isdigit())

