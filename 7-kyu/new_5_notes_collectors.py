# https://www.codewars.com/kata/58029cc9af749f80e3001e34

def get_new_notes(salary,bills):
    return max(salary - sum(bills), 0) // 5

