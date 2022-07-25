# https://www.codewars.com/kata/55147ff29cd40b43c600058b

def char_concat(word):
    string = ''
    for i in range(len(word)/2):
        string += word[i] + word[-i-1] + str(i+1)
    return string
