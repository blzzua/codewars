# https://www.codewars.com/kata/57e0206335e198f82b00001d

def esrever(string):
    if string:
        return string[-2::-1]+string[-1]
    else:
        return ''
