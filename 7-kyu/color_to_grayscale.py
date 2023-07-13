# https://www.codewars.com/kata/649c4012aaad69003f1299c1

def rgb_to_grayscale(color):
    r, g, b = [int(c,16) for c in (color[1:3], color[3:5], color[5:])]
    y = round(min(255, (0.299 * r + 0.587 * g + 0.114 * b)))
    g = hex(y)[2:4].upper().zfill(2)*3
    return f"#{g}"
