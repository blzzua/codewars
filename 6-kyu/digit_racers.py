# https://www.codewars.com/kata/682d3da198976a1e4c728d3c

def digit_racers(s):
    stat = {d: (s.count(d), s[::-1].find(d)) for d in list('0123456789')}
    places = [list() for i in range(11)]
    absent = [d for d in stat if stat[d][0] == 0]
    places[0] = absent
    prevcnt = 0
    place = 0
    for d in sorted(stat, key=lambda x: (-stat[x][0], stat[x][1])):
        if stat[d][0]:
            if stat[d][0] != prevcnt:
                place += 1
            places[place].append(d)
            prevcnt = stat[d][0]
    # formattin output
    res = ''
    if places[1] != []:
        res += '1st place: '+', '.join(places[1])+'\n'
    if places[2] != []:
        res += '2nd place: '+', '.join(places[2])+'\n'
    if places[3] != []:
        res += '3rd place: '+', '.join(places[3])+'\n'
    for i in range(4,11):
        if places[i] != []:
            res += f'{i}th place: '+', '.join(places[i])+'\n'
    if places[0] != []:
        res += 'Absent digits: '+', '.join(places[0])
    else:
        res += 'All digits present'

    return res
