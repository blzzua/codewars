# https://www.codewars.com/kata/5893e7578afa367a61000036

def almost_increasing_sequence(sequence):
    seq1 = sequence[:]
    seq2 = sequence[:]
    break_cnt = 0
    for i, (a,b) in enumerate(zip(sequence, sequence[1:])):
        if a >= b:
            if break_cnt == 0:
                seq1.pop(i)
                seq2.pop(i+1)
            break_cnt += 1
        if break_cnt > 1: # early exit with False
            return False
    
    if break_cnt == 0:
        return True
    # is removing 1 element solves problem?
    elif break_cnt == 1:
        is_increasing1 = all(a < b for a,b in zip(seq1, seq1[1:]))
        is_increasing2 = all(a < b for a,b in zip(seq2, seq2[1:]))
        return is_increasing1 or is_increasing2
    else:
        print('wtf')


