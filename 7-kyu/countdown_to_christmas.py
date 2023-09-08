# https://www.codewars.com/kata/56f6b23c9400f5387d000d48

from datetime import date

def days_until_christmas(day):
    xmas = date(day.year, 12, 25)
    if day > xmas:
        xmas = date(day.year + 1, 12, 25)
    return (xmas - day).days
