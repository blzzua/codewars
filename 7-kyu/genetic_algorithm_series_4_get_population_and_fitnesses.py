# https://www.codewars.com/kata/567b468357ed7411be00004a

def map_population_fit(population, fitness):
    return [ChromosomeWrap(chromosome=c,fitness=fitness(c)) for c in population]

