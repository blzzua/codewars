# https://www.codewars.com/kata/591404294ef3051cbe000035

def triangular_sum(n):
    for i in range(int(n**0.25)+2, 1, -1):
        if i ** 2 + i ** 4  == 2 * n:
            return True
    else:
        return False
