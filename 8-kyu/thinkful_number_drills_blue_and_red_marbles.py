# https://www.codewars.com/kata/5862f663b4e9d6f12b00003b

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start-blue_pulled)/((blue_start-blue_pulled)+(red_start-red_pulled))


