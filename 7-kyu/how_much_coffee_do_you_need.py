# https://www.codewars.com/kata/57de78848a8b8df8f10005b1

def how_much_coffee(events):
    dd = {'cw':1,'CW':2,'cat':1,'CAT':2,'dog':1,'DOG':2,'movie':1,'MOVIE':2}
    coffee = sum(dd.get(i, 0) for i in events)
    if coffee > 3:
        return 'You need extra sleep'
    return coffee

