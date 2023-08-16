# https://www.codewars.com/kata/64cac86333ab6a14f70c6fb6

def check_logs(log):
    if log == []: return 0
    cnt = 1
    prev = log[0]
    for line in log[1:]:
        if prev >= line:
            cnt+=1
        prev = line
    return cnt
