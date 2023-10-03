# https://www.codewars.com/kata/54d3bb4dfc75996c1c000c6d

def midpoint_sum(arr):
    if len(arr) < 3:
        return None
    for i in range(1,len(arr)-1):
        l = sum(arr[:i])
        r = sum(arr[i+1:])
        if l == r:
            print(i)
            return i
    else:
        return None

# almost dublicate https://www.codewars.com/kata/5679aa472b8f57fb8c000047
