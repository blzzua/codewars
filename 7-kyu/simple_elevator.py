# https://www.codewars.com/kata/52ed326b8df6540e06000029

def goto(level,button):
    print(type(level), level, type(button),)
    if not (isinstance(level,int) and isinstance(button, str)):
        return 0 # wrong type 
    if not ((0 <= level <= 3) and button in ['0','1','2','3']):
        return 0 # wrong diapason
    return int(button) - level 
        
