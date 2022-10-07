# https://www.codewars.com/kata/57cbb9e240e3024aae000b26

def code_for_same_protein(seq1,seq2):
    return all( codons.get(seq1[i: i+3], '') == codons.get(seq2[i: i+3], '') for i in range(0, len(seq1), 3))

