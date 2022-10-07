# https://www.codewars.com/kata/563c13853b07a8f17c000022

from datetime import datetime

def is_today(date): 
    return datetime.today().strftime('%F') ==  date.strftime('%F')

