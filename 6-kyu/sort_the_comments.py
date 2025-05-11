# https://www.codewars.com/kata/58a0f18091e53d2ad1000039

def sort_ranks(ranks):
    return ['.'.join(map(str,r)) for r in sorted([tuple(map(int,rank.split('.'))) for rank in ranks])]
