# https://www.codewars.com/kata/57403b5ad67e87b5e7000d1d

def bubble(l):
    res = []
    while True:
        swapped = False
        for i,(a,b) in enumerate(zip(l,l[1:])):
            if a > b:
                l[i], l[i+1] = l[i+1], l[i]
                res.append(l[::])
                swapped = True
        if not swapped:
            break
    return res

    

