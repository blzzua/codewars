# https://www.codewars.com/kata/5714803d2817ffce17000a35

def find_a_b(numbers,c):
    for i, a in enumerate(numbers[:-1]):
        for b in numbers[i+1:]:
            if a * b == c:
                return [a,b]
            
