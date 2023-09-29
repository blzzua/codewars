# https://www.codewars.com/kata/53fc954904a45eda6b00097f

class list(list):
    def even(self):
        return list(filter(lambda x: isinstance(x, int) and x % 2 == 0, self))
    def odd(self):
        return list(filter(lambda x: isinstance(x, int) and  x % 2 == 1, self))
    def under(self, value):
        return list(filter(lambda x: isinstance(x, int) and x < value, self))
    def over(self, value):
        return list(filter(lambda x: isinstance(x, int) and x > value, self))
    def in_range(self, a, b):
        return list(filter(lambda x: isinstance(x, int) and a <= x <= b, self))
