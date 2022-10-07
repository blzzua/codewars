# https://www.codewars.com/kata/5aca48db188ab3558e0030fa

def calc_type(a, b, res):
    return {a + b: 'addition',
            a - b: 'subtraction',
            a * b: 'multiplication',
            a / b: 'division'}[res]

