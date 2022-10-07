# https://www.codewars.com/kata/557d9e4d155e2dbf050000aa

class TrueClass:
    pass
def anything(thing):
    def TrueMethod(*args):
        return True
    for _comp in '__lt__', '__le__', '__eq__', '__ne__', '__ge__', '__gt__':
        setattr(TrueClass, _comp, TrueMethod)
    return TrueClass()


