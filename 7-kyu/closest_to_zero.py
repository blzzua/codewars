# https://www.codewars.com/kata/59887207635904314100007b 

def closest(lst):
    closest = min(lst, key=abs)
    if closest == 0 or -closest not in lst :
        return closest
