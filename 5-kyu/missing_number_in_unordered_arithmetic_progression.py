# https://www.codewars.com/kata/568fca718404ad457c000033
def find(seq):
    mmin = seq[0] 
    mmax = seq[0]
    llen = len(seq) +1
    ssum = 0 # fact sum
    for i in seq:
        ssum += i
        mmin = i if i < mmin else mmin
        mmax = i if i > mmax else mmax
    gsum = ( (llen) * (mmin + mmax) // 2 )  # theoretical sum
    res = gsum - ssum
    return res

