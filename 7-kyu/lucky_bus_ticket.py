# https://www.codewars.com/kata/58902f676f4873338700011f

def is_lucky(ticket):
    if ticket.isdigit() and len(ticket) == 6:
        nums = [*map(int,ticket)]
        return sum(nums[:3]) == sum(nums[3:])
    return False
