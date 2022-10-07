# https://www.codewars.com/kata/582ba36cc1901399a70005fc

def get_average(lst): 
    return round(sum([o["age"] for o in lst])/len(lst))

