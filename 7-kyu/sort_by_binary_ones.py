# https://www.codewars.com/kata/59eb28fb0a2bffafbb0000d6

def sort_by_binary_ones (numList): 
    return sorted(sorted(numList), key=lambda x: bin(x).count('1'), reverse=True)

