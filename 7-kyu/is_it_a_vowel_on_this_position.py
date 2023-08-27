# https://www.codewars.com/kata/5a2b7edcb6486a856e00005b

def check_vowel(string, position):
    w = 'aeiou'
    if 0 <= position < len(string) and string[position].lower() in w:
        return True
    else:
        return False
