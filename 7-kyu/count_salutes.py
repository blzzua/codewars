# https://www.codewars.com/kata/605ae9e1d2be8a0023b494ed

def count_salutes(hallway):
    c = 0 
    arr = hallway.replace('-', '')
    for i in range(0, len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == '><' and j > i:
                c += 2
    return c

