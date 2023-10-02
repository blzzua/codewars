# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2

def validate(n):
    digit_sum = doubled = 0
    while n:
        n, rem = divmod(n, 10)
        digit_sum, doubled = digit_sum + (doubled * rem + rem) - 9 * (rem > 4) * doubled, 1 - doubled
    return digit_sum % 10 == 0
