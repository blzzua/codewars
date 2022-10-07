# https://www.codewars.com/kata/525f039017c7cd0e1a000a26

def palindrome_chain_length(n):
    i = 0
    while True:
        n_s = str(n)
        r_s = n_s[::-1]
        if n_s == r_s:
            break
        else:
            n = int(r_s)+int(n_s)
            i += 1
        if i > 100:
            # circutbreaker
            break 
    return i

