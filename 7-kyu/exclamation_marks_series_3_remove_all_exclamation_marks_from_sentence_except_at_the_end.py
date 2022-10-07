# https://www.codewars.com/kata/57faefc42b531482d5000123

def remove(s):
    return s.replace("!", "") + "!" * (len(s) - len(s.rstrip("!")))

