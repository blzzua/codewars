# https://www.codewars.com/kata/583fd0398a20113a83000061

# kata is not translated to python yet
def findTwoUnique(inList):
    n = (len(inList)+2)//2
    a = 0
    s = 0
    for v in inList:
        a = a ^ v
        s += v
    b = n * (n+1) - s
    # now we have x = a ^ b; y = a + b; know a,b. solve for x,y:
    c = (b - a) // 2
    x = a ^ c
    y = c
    return y, x # todo check sort


findTwoUnique([1,2,4,3,5,4,2,1]) === [3,5]
findTwoUnique([1,1,2,3,3,4]) === [2,4]
findTwoUnique([9,9,8,8,7,6,5,4,3,2,1,2,3,4,5,6]) === [1,7]
