# https://www.codewars.com/kata/53f211b159c3fcec3d000efa

def left(string,i=1):
    if i == 0:
        return ''
    if isinstance(i, int):
        return string[:i]
    if isinstance(i, str):
        j = string.index(i)
        return string[:j]
    
def right(string,i=1):
    if i == 0:
        return ''
    if isinstance(i, int):
        return string[-i:]
    if isinstance(i, str):
        j = string[::-1].index(i[::-1])
        return string[-j:]
