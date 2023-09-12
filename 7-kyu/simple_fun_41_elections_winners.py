# https://www.codewars.com/kata/58881b859ab1e053240000cc

def elections_winners(votes, k):
    mm = max(votes)
    if k > 0:
        return sum(x > (mm - k) for x in votes)
    else:
        return 0 if sum(x == mm for x in votes) > 1 else 1
