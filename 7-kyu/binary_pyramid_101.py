# https://www.codewars.com/kata/5596700a386158e3aa000011

def binary_pyramid(m,n):
    return str(bin(sum(int(str(bin(i))[2:]) for i in range(m,-~n))))[2:]
        

