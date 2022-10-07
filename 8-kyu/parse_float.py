# https://www.codewars.com/kata/57a386117cb1f31890000039

def parse_float(string):
    try:
        return float(string)
    except TypeError:
        return None
    except ValueError:
        return None

