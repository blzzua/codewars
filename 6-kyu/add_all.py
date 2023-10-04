# https://www.codewars.com/kata/5b7d7ce57a0c9d86c700014b

def add_all(lst, accumulator = 0):
    if len(lst) == 1:
        return 0
    if len(lst) == 2:
        return accumulator + sum(lst)

    a, b, *lst = sorted(lst)
    return add_all(lst = [a+b] + lst, accumulator= a + b + accumulator)
