# https://www.codewars.com/kata/6507e3170b7009117e0c7865

def switch(string_prison):
    return ''.join('01'[c=='0'] for c in string_prison)
    
def freed_prisoners(prison):
    if not prison[0]: # corner case: on first closed cell
        return False

    string_prison = ''.join('01'[c] for c in prison)
    shift = free = 0 
    while string_prison:
        shift = string_prison.find('1')
        if shift >= 0:
            free += 1
            shift += 1
            string_prison = switch(string_prison[shift:])
        else:
            break
    return free

#  clever: len(list(itertools.groupby(prison))) + corner case
