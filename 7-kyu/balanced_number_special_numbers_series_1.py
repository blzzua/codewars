# https://www.codewars.com/kata/5a4e3782880385ba68000018

def balanced_num(number):
    l = len(str(number))
    if l % 2 == 0:
        if sum(int(i) for i in str(number)[:(l-1)//2]) == sum(int(i) for i in str(number)[(l+2)//2:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:
        if sum(int(i) for i in str(number)[:(l)//2]) == sum(int(i) for i in str(number)[(l+1)//2:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
        

