# https://www.codewars.com/kata/57e7d21f6603f6e31f00007c

def add(a, b = None):
    def subfunc(x):
        return a + x
    return subfunc
    

def subtract(a, b = None):
    def subfunc(x):
        return a - x
    return subfunc
    
    
def multiply(a, b = None):
    def subfunc(x):
        return a * x
    return subfunc
    

def apply(fun, b = None):
    def fun0(x):
        def fun1(y):
            return y
        return fun0(x)
    return fun
  
