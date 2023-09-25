# https://www.codewars.com/kata/64fd5072fa88ae669bf15342

def tree_photography(lst):
    mx = lst[0]
    cntr = cntl = 0
    for i in lst[1:]:
        if i > mx:
            mx = i
            cntr += 1
    mx = lst[-1]
    for i in lst[::-1][1:]:
        if i > mx:
            mx = i
            cntl += 1
    return ['left', 'right'][cntl > cntr]
