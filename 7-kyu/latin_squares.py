# https://www.codewars.com/kata/645fb55ecf8c290031b779ef

def make_latin_square(n):
    latin_square = [[ (i+j) % n +1 for i  in range(1,n+1)] for j in range(1,n+1)]
    return latin_square
