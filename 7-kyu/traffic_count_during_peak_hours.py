# https://www.codewars.com/kata/586ed2dbaa0428f791000885

def traffic_count(array):
    c1, c2, c3, c4 = ([max(array[i*6:i*6+6]) for i in range(4)])
    return [('4:00pm', c1), ('5:00pm', c2), ('6:00pm', c3), ('7:00pm', c4)]
