# https://www.codewars.com/kata/5782a87d9fb2a5e623000158

def clock_degree(s) :
    h, m = map(int,s.split(':'))
    if not ( 0 <= h < 24 and 0 <= m < 60 ):
        return 'Check your time !'
    hh = 30 * (h % 12) or 360
    mm = 6 * m or 360
    return f'{hh}:{mm}'
