# https://www.codewars.com/kata/5b37a50642b27ebf2e000010

def sum_of_a_beach(beach):
    return sum([beach.lower().count(w) for w in ["sand","water","fish","sun"]])

