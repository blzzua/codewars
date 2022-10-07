# https://www.codewars.com/kata/558ee8415872565824000007

def is_divisible(n, *args):
    return all(n % i ==0 for i in args)
        

