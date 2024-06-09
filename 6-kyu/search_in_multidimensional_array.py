# https://www.codewars.com/kata/52840d2b27e9c932ff0016ae

def ravel(iterable):
    for item in iterable:
        if type(item) == list:
            yield from ravel(item)
        else:
            yield item
            
def locate(seq, value): 
    for item in ravel(seq):
        if item == value:
            return True
    return False
