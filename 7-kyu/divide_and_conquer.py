# https://www.codewars.com/kata/57eaec5608fed543d6000021

def div_con(x):
    sum_int = sum_not = 0
    for i in x:
        if type(i) == int:
            sum_int += i
        else:
            sum_not += int(i)
    return sum_int - sum_not
  
  
# clever:
def div_con(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst)
