# https://www.codewars.com/kata/55b3425df71c1201a800009c

from statistics import median, mean
def format_time(s):
    s = int(s)
    h,s = divmod(s,3600)
    m,s = divmod(s,60)
    return f'{h:02d}|{m:02d}|{s:02d}'

def stat(strg):
    if strg == '':
        return ''
    data = []
    for time in strg.split(', '):
        h,m,s = map(int, time.split('|'))
        ss = h*3600+m*60+s
        data.append(ss)
    rng = format_time(max(data) - min(data))
    avg = format_time(mean(data))
    mdn = format_time(median(data))
    return f'Range: {rng} Average: {avg} Median: {mdn}'
  
