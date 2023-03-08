# https://www.codewars.com/kata/5856c5f7f37aeceaa100008e

def baubles_on_tree(baubles, branches):
    if branches <= 0:
        return 'Grandma, we will have to buy a Christmas tree first!'
    cnt, rem = divmod(baubles, branches)
    return [cnt+1] * rem + [cnt] * (branches - rem)
