# https://www.codewars.com/kata/546b22225874d24fbd00005b

def linked_sort(a_to_sort,a_linked, key=str):
    for i, pair in enumerate(sorted(zip(a_to_sort,a_linked), key=key)):
        (a_to_sort[i], a_linked[i]) = pair
    return a_to_sort
