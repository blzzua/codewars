# https://www.codewars.com/kata/5571f712ddf00b54420000ee

def loose_change(cents):
    res = {}
    cents = max(0,int(cents))
    for nominal, value in [('Quarters', 25), ('Dimes', 10), ('Nickels',5), ('Pennies',1)]:
        res[nominal], cents = divmod(cents, value)
    return res
