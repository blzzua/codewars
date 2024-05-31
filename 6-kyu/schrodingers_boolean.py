# https://www.codewars.com/kata/5a5f9f80f5dc3f942b002309

class MyClass():
    def __init__(self):
        pass
    
    def __eq__(self, other):
        return True

    def __bool__(self):
        return True

omnibool = MyClass()


# actually nessesary only part is:
    def __eq__(self, other):
        return True

