# https://www.codewars.com/kata/597d75744f4190857a00008d

#from collections import Counter
def paint_letterboxes(start, finish):
    l = ''.join(str(i) for i in range(start,-~finish))
    return [l.count(str(i)) for i in range(10)]

