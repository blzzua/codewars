# https://www.codewars.com/kata/57d52a7f76da830e43000188

import numpy
def sctc(sin):
    angle = numpy.arcsin(sin)
    r = [numpy.sin(angle), numpy.cos(angle), numpy.tan(angle), 1/numpy.tan(angle)]
    return [round(a,2) for a in r]
    

