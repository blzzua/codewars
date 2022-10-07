# https://www.codewars.com/kata/57475353facb0e7431000651

def hot_singles(arr1, arr2):
    index = [i for i in arr1 if i not in arr2] + [i for i in arr2 if i not in arr1]
    return [item for i, item in enumerate(index) if i == index.index(item)]
    

