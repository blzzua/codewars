# https://www.codewars.com/kata/596b8a3fc4cb1de46b000001

def center(strng, width, fill=' '):
    left = fill * ((width + 1 - len(strng)) // 2)
    right = fill * ((width - len(strng)) // 2)
    return left + strng + right

