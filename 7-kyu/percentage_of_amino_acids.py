# https://www.codewars.com/kata/59759761e30a19cfe1000024

def aa_percentage(s, acids = None):
    if acids is None:
        acids = ["A", "I", "L", "M", "F", "W", "Y", "V"]
    return round(100 * sum(c in acids  for c in s) / len(s))
