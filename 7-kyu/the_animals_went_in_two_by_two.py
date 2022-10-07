# https://www.codewars.com/kata/578de3801499359921000130

def two_by_two(animals):
    if animals:
        return {a:2 for a in animals if animals.count(a)>1} 
    else:
        return False

