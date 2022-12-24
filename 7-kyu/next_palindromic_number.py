# https://www.codewars.com/kata/56a6ce697c05fb4667000029
  
def is_pal(val):
    return str(val) == str(val)[::-1]
    
def next_pal(val):
    while True:
        val += 1
        if is_pal(val):
            return val
