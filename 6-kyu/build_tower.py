# https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors):
    return [('*'*((i*2)+1)).center((n_floors*2)-1, ' ') for i in range(n_floors)]
