# https://www.codewars.com/kata/5965144da82d479517000001

def we_rate_dogs(string, rating):
    s = string.split('/')
    return f'{s[0][:-1]}{rating}/{s[1]}'
