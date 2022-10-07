# https://www.codewars.com/kata/542ebbdb494db239f8000046

def next_item(xs, item):
    it = iter(xs)
    try:
        while next(it) != item:
            pass
        return next(it)
    except StopIteration:
        pass

