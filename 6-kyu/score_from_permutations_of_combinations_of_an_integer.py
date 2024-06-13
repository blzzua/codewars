# https://www.codewars.com/kata/5676ffaa8da527f234000025

import pip
pip.main(['install', 'more_itertools'])

import itertools
import more_itertools 

def sc_perm_comb(num):
    res =  set()
    for var in more_itertools.powerset(str(num)):
        if var:
            for comb in itertools.permutations(var):
                res.add(int(''.join(comb)))
    return sum(res)
