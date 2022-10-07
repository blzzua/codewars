# https://www.codewars.com/kata/5609fd5b44e602b2ff00003a

def process_2arrays(arr1, arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    
    return [len(s1&s2), len(s1^s2), len(s1-s2), len(s2-s1)]

