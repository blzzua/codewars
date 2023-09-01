# https://www.codewars.com/kata/598a1fc1676fdd837f000e56

def smallest_doll_size(largest_doll):
    if largest_doll() is not None:
        return smallest_doll_size(largest_doll())
    return largest_doll.size
