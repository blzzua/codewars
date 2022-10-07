# https://www.codewars.com/kata/5becace7063291bebf0001d5

def positive_to_negative(binary):
    #return binary
    return [(1-b) if 1 in binary[i:] else b for i,b in enumerate(binary, 1)]

