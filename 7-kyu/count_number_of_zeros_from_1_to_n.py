# https://www.codewars.com/kata/557cffec8c3e8e55cc00010f

def count_zeros(x):   
    return sum(str(i).count('0') for i in range(1,x+1))

# math algoritmic solution
def count_zeros(n):
    res = 0
    i = 0
    while True:
        b, c = divmod(n, i)
        a, b = divmod(b, 10)
        if a == 0:
            return res
        if b == 0:
            res += (a - 1) * i + c + 1
        else: 
            res += a * i
        i *= 10
