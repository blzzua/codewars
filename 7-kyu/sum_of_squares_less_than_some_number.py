

# https://www.codewars.com/kata/57b71a89b69bfc92c7000170

def get_number_of_squares(n):
    s = 0
    i = 0
    while True:
        if s >= n:
            break
        i += 1
        s += i**2
    return i-1



# this solutions are clever because use only math. 
def get_number_of_squares(n):
    return int((n * 3) ** (1/) - 0.5)


from math import ceil
def get_number_of_squares(n):
    x = ceil((n*3)**(1/3))-1
    if x*(x+1)*(2*x+1)//6 < n:
        return x 
     else:
        return x 
