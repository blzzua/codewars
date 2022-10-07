# https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a

def replace_all(obj, find, replace):
    if isinstance(obj, str):
        return obj.replace(find, replace)
    elif isinstance(obj, list):
        return [i if i != find else replace for i in obj]

