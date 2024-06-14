# https://www.codewars.com/kata/533ee21f69fcbb36110001d5

# this kata not traslated to python yet
# but solved

class NumClass:
    def __init__(self):
        self.value = []

    @property
    def one(self):
        self.value.append('1')
        return self
    @property
    def two(self):
        self.value.append('2')
        return self
    @property
    def three(self):
        self.value.append('3')
        return self
    @property
    def four(self):
        self.value.append('4')
        return self
    @property
    def five(self):
        self.value.append('5')
        return self
    @property
    def six(self):
        self.value.append('6')
        return self
    @property
    def seven(self):
        self.value.append('7')
        return self
    @property
    def eight(self):
        self.value.append('8')
        return self
    @property
    def nine(self):
        self.value.append('9')
        return self

    def __int__(self):
        return int(''.join(self.value))
    
    def __repr__(self):
        return repr(int(self))
        
    def __str__(self):
        return str(int(self))

    def __eq__(self, other):
        if isinstance(other, int):
            return int(self) == other
        if isinstance(other, str):
            return str(self) == other


Num = NumClass()
print(Num.seven.three.one)
# 731

Num = NumClass()
print(Num.one.two.three == 123)
# True

Num = NumClass()
print(Num.one.two.three == '123')
# True

