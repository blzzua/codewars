# https://www.codewars.com/kata/590ee3c979ae8923bf00095b

def color_2_grey(image):
    return [[ [round(sum(pixel)/3)]*3 for pixel in line ] for line in image]
