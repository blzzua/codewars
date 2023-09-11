# https://www.codewars.com/kata/6391fe3f322221003db3bad6

def perpendicular(n):
    return (n // 2) * (n // 2 + int(n % 2 == 1))

# clever math n * n // 4
