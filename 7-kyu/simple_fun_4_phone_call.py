# https://www.codewars.com/kata/588425ee4e8efb583d000088

def phone_call(min1, min2_10, min11, s):
    minutes = 0
    for i in [min1] + [min2_10]*9:
        if i <= s:
            s -= i
            minutes += 1
        else:
            return minutes
    return minutes + s // min11
