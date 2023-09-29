# https://www.codewars.com/kata/53988ee02c2414dbad000baa

def to_pretty(seconds):
    if seconds == 0:
        return 'just now'
    if seconds < 60:
        if seconds == 1:
            return f'a second ago'
        return f'{seconds} seconds ago'
    if seconds < 60*60:
        minutes = seconds // 60
        if minutes == 1:
            return f'a minute ago'    
        return f'{minutes} minutes ago'
    if seconds < 24 * 60*60:
        hours = seconds // (60 * 60)
        if hours == 1:
            return f'an hour ago'    
        return f'{hours} hours ago'
    if seconds < 7 * 24 * 60 * 60:
        days = seconds // (24 * 60 * 60)
        if days == 1:
            return f'a day ago'    
        return f'{days} days ago'
    else:
        weeks = seconds // (7 * 24 * 60 * 60)
        if weeks == 1:
            return f'a week ago'    
        return f'{weeks} weeks ago'
