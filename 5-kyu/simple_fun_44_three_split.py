# https://www.codewars.com/kata/588833be1418face580000d8

def three_split(seq):
    seq_sum = sum(seq)
    if seq_sum % 3 != 0:
        return 0
    target_sum = seq_sum // 3
    res = 0
    for i in range(1,len(seq)-1):
        if sum(seq[0:i]) != target_sum:
            continue
        for j in range(i+1, len(seq)):
            if sum(seq[i:j]) != target_sum:
                continue
            else:
                res+=1
    return res

