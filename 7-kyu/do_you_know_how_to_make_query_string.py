# https://www.codewars.com/kata/595249fc10b69f4f7a000003

def to_query_string(data):
    res = []
    for k,v in data.items():
        if type(v) == list:
            for item in v:
                res.append((k,str(item)))
        else:
            res.append( (k,str(v)) )
    return '&'.join([k+'='+v for k,v in res])

