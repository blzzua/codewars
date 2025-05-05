# https://www.codewars.com/kata/55bc0c54147a98798f00003e

def substring(strng):
    strng_len = len(strng)
    max_len = 0
    break_fl = False
    res = ''
    for i, first_letter in enumerate(strng):
        second_letter = ''
        for j in range(i, strng_len):
            if strng[j] == first_letter or (second_letter != '' and strng[j] == second_letter ):
                continue
            if second_letter == '' and strng[j] != second_letter :
                second_letter = strng[j]
            else:
                if len(strng[i:j]) > max_len:
                    res = strng[i:j]
                    max_len = len(strng[i:j])
                break_fl = True
                break
        else:
            if len(strng[i:j+1]) > max_len:
                res = strng[i:j+1]
                max_len = len(strng[i:j+1])
        if break_fl == True:
            break_fl = False
            continue
    return res
