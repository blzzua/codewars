# https://www.codewars.com/kata/57a1ae8c7cb1f31e4e000130

def get_min_max(seq): 
    # single-pass solution
    _max  = _min = seq[0] 
    for i in seq: 
        if _min > i:
            _min = i
        if _max < i:
            _max = i
    return (_min, _max)
  
