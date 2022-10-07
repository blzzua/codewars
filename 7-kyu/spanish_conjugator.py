# https://www.codewars.com/kata/5a81b78d4a6b344638000183

def conjugate(verb):
    suf_d = {'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'], 
             'er': ['o', 'es', 'e', 'emos', 'eis', 'en'], 
             'ir': ['o', 'es', 'e', 'imos', 'is', 'en']}
    return {verb: [verb[:-2] + s for s in suf_d[verb[-2:]]]}

