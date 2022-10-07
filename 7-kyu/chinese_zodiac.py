# https://www.codewars.com/kata/57a73e697cb1f31dd70000d2

def chinese_zodiac(year):
    return elements[(year - 1924) // 2 % 5] + ' ' + animals[(year - 1924) % 12]

