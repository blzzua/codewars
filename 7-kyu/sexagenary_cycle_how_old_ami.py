# https://www.codewars.com/kata/62cc917fedc75c95ef961ad1

hs = '甲乙丙丁戊己庚辛壬癸'
eb = '子丑寅卯辰巳午未申酉戌亥'

from math import gcd
def how_old(birth_year, present_year):
    # i know that this is 60, but I wanna avoid magic numbers and generate calendar dict
    cyclesize = (len(hs)*len(eb)/gcd(len(hs),len(eb))) 
    calendar = {h+e:i for i,(h,e) in enumerate( zip( hs * int(cyclesize//len(hs)), eb * int(cyclesize//len(eb))),1) }
    birth = calendar.get(birth_year) 
    present = calendar.get(present_year) 
    year = present - birth
    return (year - 1) % cyclesize + 1

# clever:
HEAVENLY_STEMS = '甲乙丙丁戊己庚辛壬癸'
EARTHLY_BRANCHES = '子丑寅卯辰巳午未申酉戌亥'
YEAR = dict(zip(map(''.join, zip(HEAVENLY_STEMS * 6, EARTHLY_BRANCHES * 5)), range(60)))
def how_old(birth_year, present_year):
    a, b = YEAR[birth_year], YEAR[present_year]
    return b - a + 60 * (a >= b)
