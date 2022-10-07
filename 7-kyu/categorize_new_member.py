# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(data):
    return ['Senior' if a>=55 and b>7 else 'Open' for a,b in data]

