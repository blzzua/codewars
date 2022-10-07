# https://www.codewars.com/kata/59ff4709ba2a14501500003a

def conv(s):
     return int(s.replace('T','000000').replace('KG','000').replace('G',''))
    
def arrange(arr):
    return sorted(arr, key=conv)


