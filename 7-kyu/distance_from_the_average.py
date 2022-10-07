# https://www.codewars.com/kata/568ff914fc7a40a18500005c

def distances_from_average(test_list):
    avg = sum(test_list)/len(test_list)
    return [round(avg-i,2) for i in test_list]

