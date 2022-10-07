# https://www.codewars.com/kata/5121303128ef4b495f000001

# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.
class Person:
    def __init__(self, my_name):
        self.name = my_name
    
    def greet(self,  your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)

