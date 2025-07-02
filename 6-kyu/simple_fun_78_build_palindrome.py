# https://www.codewars.com/kata/58942f9175f2c78f4b000108

def build_palindrome(st):
    if st == st[::-1]:
        return st
    for i in range(1,len(st)+1):
        if st[i:] == st[i:][::-1]:
            break
    return st[0:i]+ st[i:]+ st[0:i][::-1]
