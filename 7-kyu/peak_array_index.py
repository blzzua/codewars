# https://www.codewars.com/kata/5a61a846cadebf9738000076

def peak(arr):
    for i in range(len(arr)):
        if sum(arr[0:i]) == sum(arr[i+1:len(arr)]):
            return i
    return -1
    
    

