# https://www.codewars.com/kata/562d8d4c434582007300004e/solutions/python

def obfuscate(email):
    return email.replace('@', ' [at] ').replace('.',' [dot] ')
