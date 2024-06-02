# https://www.codewars.com/kata/56a115cadb39a2faa000001e

def commas(num):
    num = round(num,3)
    if num == int(num):
        num = int(num)
        return f'{num:,}'
    else:
        return f'{num:,}'
