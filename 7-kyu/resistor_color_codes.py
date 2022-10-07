# https://www.codewars.com/kata/57cf3dad05c186ba22000348

def decode_resistor_colors(bands):
    colors = bands.split()
    colors_dict = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9, 'gold': 5, 'silver': 10}
    res = (colors_dict.get(colors[0]) * 10 +  colors_dict.get(colors[1]))*10 **  colors_dict.get(colors[2])
    prefix = ''
    for pr in 'kM':
        if res // 1000 > 0:
            prefix = pr
            res /= 1000
    if float(res).is_integer():
        res = int(res)
    if len(colors) > 3:
        tol = colors_dict.get(colors[3])
    else:
        tol = 20
    return f'{res}{prefix} ohms, {tol}%'

