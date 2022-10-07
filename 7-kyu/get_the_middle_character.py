# https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    l = len(s)
    if l % 2:
        return s[l//2]
    else:
        return s[l//2-1:l//2+1]


