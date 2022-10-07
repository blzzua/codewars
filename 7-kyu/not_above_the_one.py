# https://www.codewars.com/kata/5b5097324a317afc740000fe

def binary_cleaner(seq): 
    head = []
    tail = []
    for i in range(len(seq)):
        if seq[i] > 1:
            tail.append(i)
        else:
            head.append(seq[i])
    return (head,tail)

