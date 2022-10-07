# https://www.codewars.com/kata/590ac6b9be4dff49b0000042

def convert(d): 
    d,m,s = [int(d), int(d * 60 % 60), round(d * 3600 % 60)]
    if s:
        return [d,m,s]
    elif m:
        return [d,m]
    else:
        return [d]


