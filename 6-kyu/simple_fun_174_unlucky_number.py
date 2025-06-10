# https://www.codewars.com/kata/58b65c5e8b98b2e4fa000034

def unlucky_number(n):
    res = 1
    for i in range(13, n+1, 13):
        skip = False
        orig_i = i
        while i > 0:
            i, r = divmod(i,10)
            if r == 4 or r == 7:
                skip = True
                #print("break", orig_i, r)
                break
        if skip:
            continue
        else:
            #print(orig_i)
            res += 1
    return res

