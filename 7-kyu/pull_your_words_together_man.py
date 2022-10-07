# https://www.codewars.com/kata/59ad7d2e07157af687000070

def sentencify(words):
    ret = ' '.join(words) + '.'
    return ret[0].upper()+ret[1:]

