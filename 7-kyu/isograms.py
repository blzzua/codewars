# https://www.codewars.com/kata/54ba84be607a92aa900000f1

def is_isogram(string):
    string = string.lower()
    for i in string:
        x = 0
        x = string.count(i)
        if x > 1:
            return False
    else:
        return True

