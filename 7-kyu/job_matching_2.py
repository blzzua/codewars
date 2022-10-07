# https://www.codewars.com/kata/56c2578be8b139bd5c001bd8

def match(job, candidates):
    je = bool(job['equity_max'])
    jl = set(job['locations'])
    res = []
    for c in candidates:
        if je >= c['desires_equity']:
            if c['current_location'] in jl or len(jl.intersection(c['desired_locations'])) > 0:
                res.append(c)
    return res

