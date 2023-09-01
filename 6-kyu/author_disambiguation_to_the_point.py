# https://www.codewars.com/kata/580a429e1cb4028481000019

def could_be(original, another):
    origs = set(original.split())
    anots = set(another.split())
    if anots:
        return anots.issubset(origs)
    else:
        return False
