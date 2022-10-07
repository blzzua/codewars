# https://www.codewars.com/kata/57cc79ec484cf991c900018d

def db_sort(arr): 
    return sorted(arr, key=lambda i: (isinstance(i,str),i))

