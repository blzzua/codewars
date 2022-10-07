# https://www.codewars.com/kata/58c2158ec7df54a39d00015c

def moment_of_time_in_space(moment):
    time = space = 0
    for c in moment:
        if c == '0' or not c.isdigit():
            space = space + 1
        elif c.isdigit(): #except zero
            time = time + int(c)
    return [time < space, time == space, time > space]

