# https://www.codewars.com/kata/57ee31c5e77282c24d000024

def paul(x):
    score = {'kata': 5, 'Petes kata': 10, 'life': 0, 'eating': 1}
    scores = sum(map(score.get, x))
    if scores < 40:
        return 'Super happy!'
    if scores < 70:
        return 'Happy!'
    if scores < 100:
        return 'Sad!'
    return 'Miserable!'

