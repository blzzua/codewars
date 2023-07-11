# https://www.codewars.com/kata/5b047875de4c7f9af800011b

def sentence(List_):
    return ' '.join(val for kkey, val in sorted((int(k), v) for dict_ in List_ for k, v in dict_.items()))
