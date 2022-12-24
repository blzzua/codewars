# https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed

def jumping_number(number):
    return ['Not!!','Jumping!!'][all(abs(int(a)-int(b)) == 1 for a,b in zip(str(number), str(number)[1:]))]
