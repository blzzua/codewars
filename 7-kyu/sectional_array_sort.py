# https://www.codewars.com/kata/58ef87dc4db9b24c6c000092

def sect_sort(array, start, length=0):
    if length > 0:
        sub_arr = array[start:start + length]
        return array[:start] + sorted(sub_arr) + array[start+length:]
    
    else:
        sub_arr = array[start:]
        return array[:start] + sorted(sub_arr) 
