# https://www.codewars.com/kata/5a47d5ddd8e145ff6200004e

def find_variable():
    for var in globals().keys():
        if globals()[var] == 777:
            return var
