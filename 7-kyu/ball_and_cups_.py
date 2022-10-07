# https://www.codewars.com/kata/5b715fd11db5ce5912000019

def cup_and_balls(b, arr):
    for left, right in arr:
        if b == left:
            b = right
        elif b == right:
            b = left
    return b

