# https://www.codewars.com/kata/5a86073fb17101e453000258

EMO = [':D', ':)', ':|', ':(', 'T_T']

def sort_emotions(arr, order):
    return sorted(arr, key=EMO.index, reverse=not order)

