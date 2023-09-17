# https://www.codewars.com/kata/589ac16a0cccbff11d000115

def segment_cover(A, L):
    A.sort()
    cnt = 1
    segment = A[0]
    for i in A:
        if segment + L < i:
            segment = i
            cnt += 1
    return cnt
