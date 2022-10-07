# https://www.codewars.com/kata/59b710ed70a3b7dd8f000027

def is_all_possibilities(arr):
    if arr and sorted(arr) == list(range(len(arr))):
        return True
    else: 
        return False

    

