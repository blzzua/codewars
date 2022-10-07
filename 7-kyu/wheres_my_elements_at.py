# https://www.codewars.com/kata/5a0ec343c374cb6da0000006

def element_location(begin: int, end: int, index: int, size: int) -> int:
    end_index = begin + index * size
    if any((end_index > end - size,  index < 0, size <= 0)):
        raise IndexError
    else:
        return end_index

