# https://www.codewars.com/kata/609eee71109f860006c377d1

def last_survivor(letters, coords): 
    letters = list(letters)
    for i in coords:
        letters.pop(i)
    return ''.join(letters)


