# https://www.codewars.com/kata/568dc014440f03b13900001d

def get_drink_by_profession(param):
    d = {
        'Jabroni': 'Patron Tequila', 
        'School counselor': 'Anything with Alcohol',
        'Programmer': 'Hipster Craft Beer', 
        'Bike gang member': 'Moonshine',
        'Politician': 'Your tax dollars', 
        'Rapper': 'Cristal'}
    return d.get(param.capitalize(), 'Beer')

