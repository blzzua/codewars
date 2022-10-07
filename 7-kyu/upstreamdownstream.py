# https://www.codewars.com/kata/58162692c2a518f03a000189

def time(distance,boat_speed,stream):
    dir, speed  = stream.split(' ')
    str_sp = int(speed) * (-1 if dir == 'Upstream' else 1)
    return round(distance/(boat_speed + str_sp),2)

