# https://www.codewars.com/kata/5b8dc84b8ce20454bd00002e

def is_tune(notes):
    cnt = 0
    for i in range(len(notes)):
        for j in range(len(notes)):
            if (notes[j]-notes[i]) % 12 in (0,2,4,6,7,9,11):
                cnt += 1
            else:
                cnt = 0
                break
        if cnt == len(notes):
            return True
    return False
