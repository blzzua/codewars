# https://www.codewars.com/kata/5c22954a58251f1fdc000008

GLYPHS = " .,:;xyYX"
GMAP = {i: GLYPHS[i * 8 // 255] for i in range(256)}

def image2ascii(image):
    return '\n'.join([''.join(map(GMAP.get, row)) for row in image])

