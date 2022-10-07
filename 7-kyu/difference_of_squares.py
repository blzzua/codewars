# https://www.codewars.com/kata/558f9f51e85b46e9fa000025

def difference_of_squares(n):
    return (n*(n+1)/2)**2-sum(i**2 for i in range(n+1))

