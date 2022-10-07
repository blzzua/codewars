# https://www.codewars.com/kata/5865cff66b5699883f0001aa

def to_time(seconds):
    h = seconds // 3600
    m = (seconds - 3600 * h) // 60
    return f'{h} hour(s) and {m} minute(s)'

