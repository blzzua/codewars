# https://www.codewars.com/kata/643ea1adef815316e5389d17

def quadrant_segment(A, B):
    return  any((x>0 or y>0) and (x<0 or y<0) for x,y in zip(A, B))
