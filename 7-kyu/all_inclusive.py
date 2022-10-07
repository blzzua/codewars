# https://www.codewars.com/kata/5700c9acc1555755be00027e

def contain_all_rots(strng, arr):
    return all(strng[i:] + strng[:i] in arr for i in range(len(strng)))

