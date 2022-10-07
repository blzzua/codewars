# https://www.codewars.com/kata/57efab9acba9daa4d1000b30

def bald(s):
    cnt = s.count('/')
    s = s.replace('/','-')
    if cnt == 0: 
        return [s, 'Clean!']
    elif cnt == 1: 
        return [s, 'Unicorn!']
    elif cnt == 2 : 
        return [s, 'Homer!']
    elif cnt < 6: 
        return [s, 'Careless!']
    else: 
        return [s, 'Hobo!']
    

