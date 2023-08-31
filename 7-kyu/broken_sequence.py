# https://www.codewars.com/kata/5512e5662b34d88e44000060

def find_missing_number(sequence):
    try:
        sorted_seq = sorted(map(int,sequence.split()))
        for a, b in zip(range(1, len(sorted_seq) + 2), sorted_seq):
            if a != b:
                return a
        return 0
    except ValueError as e:
        return 1

