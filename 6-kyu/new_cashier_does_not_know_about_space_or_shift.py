# https://www.codewars.com/kata/5d23d89906f92a00267bb83d

import re
def get_order(order):
    items = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    regex = '(' + '|'.join(items) + ')'
    order_items = [s.capitalize() for s in re.findall( regex, order, re.MULTILINE | re.IGNORECASE)]
    order_items.sort(key=lambda x: items.index(x))
    return ' '.join(order_items)
