# https://www.codewars.com/kata/57e1857d333d8e0f76002169

#Remember you have a CHANGE dictionary to work with ;)

def change_count(change):
    res = round(sum(CHANGE.get(i) for i in change.split()) % 100,2)
    return f'${res:.2f}' 

