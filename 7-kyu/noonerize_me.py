# https://www.codewars.com/kata/56dbed3a13c2f61ae3000bcd

def noonerize(numbers):
    if all(type(n) == int for n in numbers):
        a, b = numbers
        return abs(int(str(b)[0] + str(a)[1:]) - int(str(a)[0] + str(b)[1:]))
    else:
        return "invalid array"


