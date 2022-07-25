# https://www.codewars.com/kata/55563df50dda59adf900004d
def validate_ean(code):
    d = list(map(int, code))
    return (sum(d[0::2]) + sum(d[1::2]) * 3) % 10 == 0
