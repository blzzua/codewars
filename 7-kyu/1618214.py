# https://www.codewars.com/kata/5effa412233ac3002a9e471d

def add(num1, num2):
    num1, num2 = str(max(num1, num2)), str((min(num1, num2)))
    num2 = str(num2).zfill(len(num1))
    return int(''.join([str(int(a)+int(b))for a,b in zip(num1, num2)]))

