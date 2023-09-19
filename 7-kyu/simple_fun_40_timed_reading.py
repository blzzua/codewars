# https://www.codewars.com/kata/588817db5fb13af14a000020

def timed_reading(max_length, text):
    text = text.replace('?', '').replace("'",'')
    return sum(1 for i in text.split() if len(i) <= max_length)
