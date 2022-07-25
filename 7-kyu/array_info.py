# https://www.codewars.com/kata/57f12b4d5f2f22651c00256d

def array_info(x):
    if x == []:
        return 'Nothing in the array!' # totaly ugly check 
    
    return [
            [len(x)],
            [sum(1 for i in x if type(i) is int) or None],
            [sum(1 for i in x if type(i) is float) or None],
            [sum(1 for i in x if type(i) is str and i != ' ') or None],
            [sum(1 for i in x if i == ' ') or None ],
           ]
  
# best pratice
def array_info(x):
    if not x:
        return 'Nothing in the array!'
    return [
        [len(x)],
        [sum(isinstance(i, int) for i in x) or None],
        [sum(isinstance(i, float) for i in x) or None],
        [sum(isinstance(i, str) and not i.isspace() for i in x) or None],
        [sum(isinstance(i, str) and i.isspace() for i in x) or None],
    ]
