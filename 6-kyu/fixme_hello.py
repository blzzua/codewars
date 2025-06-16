# https://www.codewars.com/kata/5b0a80ce84a30f4762000069

class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
        self._order = []
    
    def setAge(self, age):
        if not 'age' in self._order:
            self._order.append('age')
        self.age = age
        return self
        
    def setSex(self, sex):
        if not 'sex' in self._order:
            self._order.append('sex')
        self.sex = sex
        return self
        
    def setName(self, name):
        if not 'name' in self._order:
            self._order.append('name')
        self.name = name
        return self
        
    def hello(self):
        sentences = ['Hello.']
        for prop in self._order:
            if prop == 'age':
                sentences.append(f'I am {self.age}.')
            if prop == 'sex':
                full_sex_str = "male" if self.sex=='M' else "female"
                sentences.append(f'I am {full_sex_str}.')
            if prop == 'name':
                sentences.append(f'My name is {self.name}.')
        return ' '.join(sentences)
