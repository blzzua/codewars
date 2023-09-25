# https://www.codewars.com/kata/574e4175ff5b0a554a00000b

import fractions # python way

def convert_to_mixed_numeral(parm):
    orig_denom = int(parm.split('/')[-1])
    orig_sign = -1 if '-' in parm else 1
    parm = parm.strip('-')
    f = fractions.Fraction(parm)
    nom, denom = f.numerator, f.denominator

    if denom == 1:
        return f'{nom*orig_sign}'

    # do not reduce fractions. undo it.
    if orig_denom != {denom}:
        coef = orig_denom//denom
        nom *= coef
        denom *= coef

    if nom > denom:
        i, nom =  divmod(nom, denom) 
        return f'{i*orig_sign} {nom}/{denom}'
    else:
        return f'{nom*orig_sign}/{denom}'
