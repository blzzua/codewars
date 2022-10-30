# https://www.codewars.com/kata/582887f7d04efdaae3000090

def find_senior(lst): 
    max_age = max(o['age'] for o in lst)
    return list(filter(lambda o: o['age'] == max_age, lst))
