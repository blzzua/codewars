# https://www.codewars.com/kata/5a8328fefd57777fa3000072

def will_it_balance(stick, terrain):
    center = sum(i * el for i, el  in enumerate(stick)) / sum(stick)
    left = terrain.index(1)
    
    for right in range(len(terrain) -1, -1, -1):
        if terrain[right] == 1:
            break

    if left <= center <= right:
        return True
    else:
        return False

# absolutly cool same solution from Mercy Madmask but use libraries:
from scipy.ndimage.measurements import center_of_mass
from math import floor, ceil
from numpy import array
def will_it_balance(stick, terrain):
    center = center_of_mass(array(stick))[0]
    return terrain[floor(center)] == 1 and terrain[ceil(center)] == 1
