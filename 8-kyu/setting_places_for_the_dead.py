# https://www.codewars.com/kata/6646c0c08b97085ca216d346

def put_close_to(place, dead, res):
    place = place - 1
    print(f'placed {dead} to {place}')
    for i in range(7):
        place_before = (24+place-i)%12
        if res[place_before] == '_____':
            res[place_before] = dead
            return res
        place_after = (24+place+i)%12
        if res[place_after] == '_____':
            res[place_after] = dead
            return res
    print(f'sorry {dead=}, no free place')
    return res

def set_table(the_dead):
    res = ['_____'] * 12
    for c in the_dead:
        print(c[0])
        if c[0] in 'QUTHCRDMZ':
            res = put_close_to(1, c, res)
        if c[0] in 'WEVOXING':
            res = put_close_to(4, c, res)
        if c[0] in 'JFABKPLY':
            res = put_close_to(7, c, res)
        if c[0] == 'S':
            res = put_close_to(10, c, res)
    return res
