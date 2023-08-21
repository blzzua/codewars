# https://www.codewars.com/kata/5645b24e802c6326f7000049

def get_a_down_arrow_of(n):
    return '\n'.join([' '* (n-j) + ''.join([str(i%10) for i in range(1, j)]) + ''.join([str(i%10) for i in range(j, 0, -1)]) 
        for j in range(n,0,-1)])
