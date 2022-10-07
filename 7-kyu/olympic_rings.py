# https://www.codewars.com/kata/57d06663eca260fe630001cc

def olympic_ring(string):
    rings = 'ADOPQRabdegopq'
    num = sum(map(lambda x: 1 if x in rings else 2 if x == 'B' else 0, string)) // 2
    if num <= 1:
        return 'Not even a medal!'
    elif num == 2: 
        return 'Bronze!'
    elif num == 3:
        return 'Silver!'
    elif num > 3:
        return 'Gold!'


