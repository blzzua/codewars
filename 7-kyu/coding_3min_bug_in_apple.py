# https://www.codewars.com/kata/56fe97b3cc08ca00e4000dc9

def sc(apple):
    for j, line in enumerate(apple):
        for i, fruit in enumerate(line):
            if fruit == 'B':
                return [j,i]
