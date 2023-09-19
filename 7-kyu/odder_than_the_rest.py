# https://www.codewars.com/kata/5983cba828b2f1fd55000114

def odd_one(arr):
    for i, c in  enumerate(arr):
        if c % 2:
            return i
    else:
        return -1
