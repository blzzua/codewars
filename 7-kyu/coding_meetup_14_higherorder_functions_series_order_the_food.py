# https://www.codewars.com/kata/583952fbc23341c7180002fd

from collections import Counter
def order_food(lst): 
    return Counter([o['meal'] for o in lst])

