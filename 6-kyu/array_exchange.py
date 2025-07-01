# https://www.codewars.com/kata/5353212e5ee40d4694001114/solutions

def exchange_with(a, b):
    buffer = []
    while a:
        buffer.append(a.pop())
    while b:
        a.append(b.pop())
    b.extend(buffer)
