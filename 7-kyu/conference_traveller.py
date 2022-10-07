# https://www.codewars.com/kata/56f5594a575d7d3c0e000ea0

def conference_picker(cities_visited, cities_offered):
    for i in cities_offered:
        if i not in cities_visited:
            return i
    return 'No worthwhile conferences this year!'

