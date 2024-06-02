# https://www.codewars.com/kata/5cd4aec6abc7260028dcd942

def shortest_steps_to_num(num):
    res = 0
    while num > 1:
        # imaging binary representation num. 
        # very digit is doubling (I am incrementing res)
        # every 1 bit is addition of 1
        num, plus1 = divmod(num,2) 
        res += plus1 + 1
    return res
