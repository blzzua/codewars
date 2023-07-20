# https://www.codewars.com/kata/59b0a6da44a4b7080300008a

def to24hourtime(hour, minute, period):
    if period == 'pm' and hour < 12:
        hour += 12
    if period == 'am' and hour == 12:
        hour = 0
    return f'{hour:02d}{minute:02d}'
