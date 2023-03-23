# https://www.codewars.com/kata/632408defa1507004aa4f2b5

def travel(total_time, run_time, rest_time, speed):
    cycles, rem = divmod(total_time, run_time + rest_time)
    res = ( cycles * run_time + min(rem, run_time) ) * speed
    return res
