# https://www.codewars.com/kata/62eb800ba29959001c07dfee

def brightest(colors):
    return max(colors, key=lambda color: max(color[1:3],color[3:5],color[5:7]))

    
    

