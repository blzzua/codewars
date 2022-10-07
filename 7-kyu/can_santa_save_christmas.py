# https://www.codewars.com/kata/5857e8bb9948644aa1000246

def determine_time(arr):
    h, m, s= 0, 0, 0
    for i in arr:
        h += int(i.split(':')[0])
        m += int(i.split(':')[1])
        s += int(i.split(':')[2])
    return 3600*h + 60*m + s <= 24 * 3600


