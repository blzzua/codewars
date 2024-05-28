# https://www.codewars.com/kata/65c6fa8551327e0ac12a191d

def is_time_good(time):
    hh, mm, ss = time.split(':')
    h, m, s = map(int,(hh, mm, ss))
    d1 = m - h; d2 = s - m
    
    if d1 == d2 and d1 in (0,1,2):
        return True # rule 1

    if d1 == d2 and h % 10 == m % 10 == s %10:
        return True  # rule 2
    
    if d1 == d2 and abs(d1) == h:
        return True  # rule 3

    if (hh + mm + ss) == (hh + mm + ss)[::-1]:
        return len(set(hh + mm + ss)) <= 2 # rule 4
    
    if time == '12:34:56':
        return True # rule 5
    
    return False
    
def next_time(time):
    h,m,s = map(int, time.split(':'))
    next_t = (h * 3600 + m * 60 + s + 1) % (60*60*24)
    hh, next_t = divmod(next_t, 3600)
    mm, ss = divmod(next_t, 60)
    return f'{hh:02d}:{mm:02d}:{ss:02d}'
        
def next_good_time(current_time):
    while True:
        current_time = next_time(current_time)
        if is_time_good(current_time):
            return current_time

# good practice is precomputed list of good times:
current_time = '00:00:00'
good = [current_time,]
while current_time < '23:59:59':
    current_time = next_time(current_time)
    if is_time_good(current_time):
        good.append(current_time)

from bisect import bisect_right
def next_good_time(current_time):
    try:
        return good[bisect_right(good, current_time)]
    except:
        return "00:00:00"
