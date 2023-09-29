# https://www.codewars.com/kata/58373ba351e3b615de0001c3

def mormons(n, reach, target):
    cnt = 0
    while n < target:
        n, cnt  = n * (reach+1), cnt + 1
    return cnt
