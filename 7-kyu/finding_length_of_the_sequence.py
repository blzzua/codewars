# https://www.codewars.com/kata/5566b0dd450172dfc4000005

def length_of_sequence(arr,n):
    n_index = [i for i, a in enumerate(arr) if a == n]
    if len(n_index) == 2:
        return n_index[1]-n_index[0]+1
    else:
        return 0

