# https://www.codewars.com/kata/5aee86c5783bb432cd000018

def hydrate(drink_string): 
    n = sum([int(i) for i in drink_string if i.isnumeric()])
    return f'{n} glass{"" if n==1 else "es"} of water'

