# https://www.codewars.com/kata/587d7544f1be39c48c000109

import numpy as np
def harvester_rescue(data):
    worm, harv, carr = np.array(data['worm'][0]), np.array(data['harvester']), np.array(data['carryall'][0])
    worm_dist = np.linalg.norm(worm - harv)
    carr_dist = np.linalg.norm(carr - harv)
    time_to_lift = 1
    if worm_dist/data['worm'][1] > carr_dist/data['carryall'][1] + time_to_lift:
        return 'The spice must flow! Rescue the harvester!'
    else:
        return 'Damn the spice! I\'ll rescue the miners!'
