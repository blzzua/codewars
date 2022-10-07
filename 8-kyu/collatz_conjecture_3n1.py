# https://www.codewars.com/kata/577a6e90d48e51c55e000217

def hotpo(n):
    cnt = 0
    while n != 1:
        if n % 2 != 0:
            n = n*3 + 1
        else:    
            n /= 2
        cnt += 1
    return cnt


