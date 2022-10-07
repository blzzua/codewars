# https://www.codewars.com/kata/5637b03c6be7e01d99000046

def make_password(phrase):
    res = ''.join(w[0] for w in phrase.split())
    res = res.translate(str.maketrans('iIoOsS', '110055'))
    return res

