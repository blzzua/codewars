# https://www.codewars.com/kata/5897cdc26551af891c000124

Q = [None, 1, 1]

def hofstadter_q(n):
    if n < len(Q) - 1 :
        return Q[n]
    i = len(Q) # else: compute
    while i <= n+1:
        Q.append(Q[i - Q[i-1]] + Q[i - Q[i-2]])
        i=i+1
    return Q[n]
