# https://www.codewars.com/kata/62bdd252d8ba0e0057da326c

letters = 'abcdefghijklmnopqrstuvwxyz'
e = {c:i for i,c in enumerate(letters,1)}
d = {i:c for i,c in enumerate(letters,1)}

def encrypt(word, n):
    r = [e.get(c) for c in word] 
    for _ in range(n):
        r = [i * 3 - 5 for i in r]
    return r

def decrypt(encrypted_word, n):
    r = encrypted_word[:]
    for _ in range(n):
        r = [(i+5)//3 for i in r]
    return ''.join(d.get(c) for c in r)
