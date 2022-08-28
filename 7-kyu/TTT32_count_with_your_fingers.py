# https://www.codewars.com/kata/57add740e298a7a6d500000d

def which_finger(n):
    a = 'Thumb'
    b = 'Index finger'
    c = 'Middle finger'
    d = 'Ring finger'
    e = 'Little finger'
    order = [ b, c, d, e, d, c, b, a ] 
    i = ( n - 2 ) % len (order)
    return order[i]
