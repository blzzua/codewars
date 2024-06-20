# https://www.codewars.com/kata/6277a3342c28814667504250
"""Is there enough ink?
Is there enough ink for printing the image?
You will get an image and the level of ink for each primary color in the tank of the printer. The image is a matrix where each cell is the color of a pixel. The color is a string of a RGB hexadecimal notation (e.g white is 'ffffff' and black is '000000'). Each primary color is a integer.
A pixel with the color code 'fefdfc' need 1 unit of Red, 2 units of Green and 3 units of Blue.
A pixel with the color code '00ff01' need 255 units of Red, 0 units of Green and 254 units of Blue.
The image is two dimensional. E.g: image = [["ffffff", "ffffff"], ["ffffff", "ffffff"]]
Your task is to determine if they are enough ink in the tank to print the image.
If the ink is enough, the "enough_ink()" function should return True. False otherwise.
Have fun!
"""


def enough_ink(image, r, g, b):
    for line in image:
        for pixel in line:
            pr, pg, pb = [255 - int(value, 16) for value in (pixel[0:2], pixel[2:4], pixel[4:6])]
            r, g, b = r - pr, g - pg, b - pb
    return all(ink >= 0 for ink in (r, g, b))
