# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

def find_next_square(sq):
    n = int(sq**0.5)
    if n**2 == sq:
        return (n+1)**2
    else:
        return -1
    


