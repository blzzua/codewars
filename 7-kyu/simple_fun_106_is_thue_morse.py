# https://www.codewars.com/kata/589a9792ea93aae1bf00001c

def thue_morse_gen():
    seq = [False]
    while True:
        for element in seq[len(seq)//2:]:
            yield int(element)
        seq.extend([not element for element in seq])    
def is_thue_morse(seq):
    g = thue_morse_gen()
    return all(a==b for a,b in zip(g,seq))
