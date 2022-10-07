# https://www.codewars.com/kata/5701800886306a876a001031

def lineup_students(string):
     return sorted(string.split(), reverse=True, key=lambda w: (len(w), w))

