# https://www.codewars.com/kata/547274e24481cfc469000416

class Human:
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        pass

class Woman(Human):
    def __init__(self):
        pass
    
def God():
    man = Man()
    woman = Woman()
    return [man, woman]


