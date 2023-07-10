# https://www.codewars.com/kata/57faa6ff9610ce181b000028

def crap(garden, bags, cap):
    caps = bags * cap
    for line in garden:
        if 'D' in line:
            return 'Dog!!'
        caps = caps - line.count('@')
    if caps >=0:
        return 'Clean'
    else:
        return 'Cr@p'
