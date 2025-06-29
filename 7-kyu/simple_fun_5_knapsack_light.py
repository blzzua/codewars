# https://www.codewars.com/kata/58842a2b4e8efb92b7000080

def knapsack_light(value1, weight1, value2, weight2, max_w):
    match (weight1 <= max_w, weight2 <= max_w, weight1 + weight2 <= max_w):
        case (True, True, True):
            return value1 + value2
        case (True, True, False):
            return max(value1, value2)
        case (True, False, False):
            return value1
        case (False, True, False):
            return value2
        case (False, False, False):
            return 0
        case _:
            print(weight1 <= max_w, weight2 <= max_w, weight1 + weight2 <= max_w)
            raise ValueError
            
