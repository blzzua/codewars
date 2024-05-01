# https://www.codewars.com/kata/5416f1834c24604c46000696

def cycle(sequence):
    seq = sequence[:]
    n = len(seq)
    for i in range(n):
        for j in range(1, int((n-i)//2+1)):
            if seq[i:i+j] == seq[i+j:i+j+j]:
                return [i, j]
    return []

#clever:
for j, x in enumerate(seq):
    i = seq.index(x)
    if 0 <= i < j:
        return [i, j - i]
