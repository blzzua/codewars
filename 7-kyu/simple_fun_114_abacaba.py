# https://www.codewars.com/kata/589d237fdfdef0239a00002e

from  string import ascii_lowercase as al
def abacaba(k):
    s = 0
    for i in bin(k-1)[::-1]:
        if i == '1':
            s+=1
        else:
            break
    return al[s]
