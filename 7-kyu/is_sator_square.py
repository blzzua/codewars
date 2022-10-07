# https://www.codewars.com/kata/5cb7baa989b1c50014a53333

def is_sator_square(tablet):
    if tablet == [line[::-1] for line in tablet][::-1] and\
       tablet == [*(map(list, zip(*tablet)))]:
        return True
    else:
        return False
        

