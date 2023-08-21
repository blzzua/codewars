# https://www.codewars.com/kata/56fac4cfda8ca6ec0f001746

def day_and_time(mins):
    day = 24 * 60
    max_mins = 7 * day
    mins = mins %  max_mins
    if mins  < 0:
        mins += max_mins
    hh, mm = divmod(mins, 60)
    wd, hh = divmod(hh, 24)
    weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday'][wd]
    return f'{weekday} {str(hh).zfill(2)}:{str(mm).zfill(2)}'
