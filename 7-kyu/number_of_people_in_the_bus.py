# https://www.codewars.com/kata/5648b12ce68d9daa6b000099

def number(bus_stops):
    return sum(i[0] - i[1] for i in bus_stops)

