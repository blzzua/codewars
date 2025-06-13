# https://www.codewars.com/kata/572f32ed3bd44719f8000a54

def sum_pow_dig_seq(start, n, k):
    seq = [start,]
    number = start
    res = False
    for i in range(k):
        number = sum(int(i) ** n for i in str(number))
        if number in seq and not res:
            i = seq.index(number)
            sub_seq = seq[i:]
            res = [i, sub_seq, len(sub_seq)]
        seq.append(number)
    if res:
        return res + [number]
    return []

