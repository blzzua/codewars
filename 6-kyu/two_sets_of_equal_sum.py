# https://www.codewars.com/kata/647518391e258e80eedf6e06

def create_two_sets_of_equal_sum(n):
    total_sum = (n * (n + 1)) // 2
    if total_sum % 2 == 1:
        return []
    s1 = []
    s2 = []
    half_left = total_sum // 2
    i = n
    while i > 0:
        if i <= half_left :
            s1.append(i)
            half_left -= i
        else:
            s2.append(i)
        i -= 1
    return s1, s2
