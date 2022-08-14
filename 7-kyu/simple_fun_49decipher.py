# https://www.codewars.com/kata/5888514674b58e929a000036

def decipher(cipher):
    l = list(cipher)
    codes = []
    while l:
        c = l.pop() 
        c = l.pop() + c 
        if int(c) < 60:
            c =  l.pop() + c 
        codes.append(int(c))
    return ''.join(map(chr,codes))[::-1]


# clever
def decipher(cipher):
    return re.sub(r'1?\d\d', lambda m: chr(int(m.group())), cipher)
