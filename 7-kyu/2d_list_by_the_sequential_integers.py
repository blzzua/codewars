# https://www.codewars.com/kata/5a8897d4ba1bb5f266000057/train/python

def make_2d_list(head,row,col):
    res = []
    for a in range(row):
        line = []
        for b in range(col):
            line.append(head)
            head+=1
        res.append(line)
    return res

