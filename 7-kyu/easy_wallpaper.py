# https://www.codewars.com/kata/567501aec64b81e252000003

from math import ceil
def wallpaper(l, w, h):
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty" ]
    area = l * w * h
    if area == 0:
        return "zero"
    else:
        return numbers[ceil(((l*h + w*h)*2 * 1.15) / 5.2)]

