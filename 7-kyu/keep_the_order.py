# https://www.codewars.com/kata/582aafca2d44a4a4560000e7

def keep_order(ary, val):
    i = 0
    if len(ary) == 0 or ary[0] >= val:
        return i
    for val1, val2 in zip(ary, ary[1:]):
        i+=1
        print(i,val1 , val ,  val2)
        if val1 < val <= val2:
            return i
    else:
        return i+1
