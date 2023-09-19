# https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef

def find_children(santas_list, children):
    res = [c for c in children if c in santas_list]
    return sorted(res)
