# https://www.codewars.com/kata/640dee7cbad3aa002e7c7de4

import math 
def buses(kids, adults, places):
    if kids < 0 or adults <= 0 or places <= 0 or (places <= 2 and kids > 0) :
        print("wrong arguments", f"{kids=}, {adults=}, {places=}")
        return 0 
    
    if kids > 0 and adults < math.ceil(kids / (places - 2)) * 2:
        print("no enouch adults")
        return 0 
    
    return math.ceil( (kids + adults) / places )
