# https://www.codewars.com/kata/57eb936de1051801d500008a

def explode(arr):  
    res = [n for n in arr if isinstance(n, int)]
    if res:
        return [arr] * sum(res) 
    else:
        return 'Void!'

