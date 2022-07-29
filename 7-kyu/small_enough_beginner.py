# https://www.codewars.com/kata/57cc981a58da9e302a000214

def small_enough(array, limit):
    return all(a <= limit for a in array)

# clever:
def small_enough(array, limit):
    return max(array)<=limit
