# https://www.codewars.com/kata/530017aac7c0f49926000084

def pluck(objs, name): 
    return [obj.get(name, None) for obj in objs]

