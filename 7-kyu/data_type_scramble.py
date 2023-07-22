# https://www.codewars.com/kata/5e5acfe31b1c240012717a78

def make_model_year(lst):
    for val in lst:
        if isinstance(val, int) and not isinstance(val, bool):
            year = val
        elif isinstance(val, tuple):
            model = ' '.join(val)
        elif isinstance(val, str):
            make = val
        elif isinstance(val, bool):
            new = val
    return {'make': make, 'model': model, 'year': year, 'new': new}
