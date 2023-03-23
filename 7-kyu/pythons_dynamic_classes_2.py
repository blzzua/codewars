# https://www.codewars.com/kata/55ddcef532f8678af1000006

def name_valid(name):
    return name[0].isupper() and name.isalnum()

class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        if name_valid(new_name):
            cls.__name__ = new_name
        else:
            raise NameError
        
    @classmethod
    def __str__(cls):
        return f'Class name is: {cls.__name__}'
