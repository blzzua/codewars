# https://www.codewars.com/kata/58279e13c983ca4a2a00002a

def greet_developers(lst): 
    res_l = []
    for d in lst:
        res_d = {}
        for k, v in d.items():
            res_d[k] = v
        res_d['greeting'] = f'''Hi {d.get('firstName')}, what do you like the most about {d.get('language')}?'''
        res_l.append(res_d)
    return res_l

