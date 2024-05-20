# https://www.codewars.com/kata/5816f2580e80c5e075000a4f

from math import gcd
    
def add_fracs(*args):
    if not args:
        return ''
    res = {'nom': 0, 'denom': 1}
    for s in args:
        nom, denom = map(int,s.split('/'))
        res_top = res['denom'] * nom + res['nom'] * denom
        res_bottom = res['denom'] * denom
        cd = gcd(res_top, res_bottom)
        if cd == 1:
            res['nom'] = res_top 
            res['denom'] = res_bottom 
        else:
            res['nom'] = res_top // cd 
            res['denom'] = res_bottom // cd
    nom, denom = res.values()
    match    (nom, denom):
        case (0  , 0    ): return ""
        case (nom, 1    ): return  f"{res['nom']}"
        #case (0  , denom): return  f"0"
        case _: return  f"{res['nom']}/{res['denom']}"
        
