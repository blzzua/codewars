# https://www.codewars.com/kata/56b97b776ffcea598a0006f2

def bubblesort_once(l):
    l = l[:] # :evil:
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    return l
        

