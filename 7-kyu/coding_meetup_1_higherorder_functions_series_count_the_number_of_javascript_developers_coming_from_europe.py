# https://www.codewars.com/kata/582746fa14b3892727000c4f

def count_developers(lst):
    return len(list(filter(lambda d:  d['language'] == 'JavaScript' and d['continent'] == 'Europe', lst)))
    

