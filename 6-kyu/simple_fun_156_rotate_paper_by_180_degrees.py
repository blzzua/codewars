# https://www.codewars.com/kata/58ad230ce0201e17080001c5

def rotate_paper(number):
    map_ = {'1': 'X', '2': '2', '3': 'X', '4': 'X', '5': '5', '6': '9', '7': 'X', '8': '8', '9': '6', '0': '0'}
    for ch1, ch2 in zip(number, number[::-1]):
        if map_.get(ch1) != ch2:
            return False
    return True
