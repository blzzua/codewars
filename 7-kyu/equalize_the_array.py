# https://www.codewars.com/kata/580a1a4af195dbc9ed00006c

def equalize(arr):
    def format(i):
        if i >= 0:
            return '+'+str(i)
        else:
            return str(i)
        
    if arr:
        return [format(i-arr[0]) for i in arr]
    else:
        return []

