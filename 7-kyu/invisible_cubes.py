# https://www.codewars.com/kata/560d6ebe7a8c737c52000084
  
def not_visible_cubes(n):
    return max(0, n**3-6*(n-1)*(n-1)-2)
