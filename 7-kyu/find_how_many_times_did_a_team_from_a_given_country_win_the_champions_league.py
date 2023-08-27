# https://www.codewars.com/kata/581b30af1ef8ee6aea0015b9

def countWins(winnerList, country):
    return sum((1 for row in winnerList if row['country'] == country), 0)
