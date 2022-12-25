# https://www.codewars.com/kata/6376bbc66f2ae900343b7010

def movie_times(open, close, length):
    start_m = open * 60 
    close_m = (close if close > open else close + 24) * 60 - length
    cur_m = start_m
    res = []
    while cur_m <= close_m:
        h, m = divmod(cur_m, 60)
        h = h % 24
        res.append((h, m))
        cur_m = cur_m + length + 15
    return res
