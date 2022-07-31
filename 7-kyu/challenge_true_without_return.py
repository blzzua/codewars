# https://www.codewars.com/kata/57e524847fbcc9300300004c
# 
# There's not much explaining for this kata.
# 
# Make it so if I call solve() it gives an output of True.
# 
# But you are not allowed to use the return keyword!
# 
# If you do disregard the challenge, at least look at others solutions for learning value.
# 
# Good luck!




solve = lambda: True

# other: 
"""Magic Functions"""
#solve = True.__nonzero__       # Python 2
solve = True.__bool__        # Python 3
solve = [1].__len__
solve = (1).__index__
solve = (1).__trunc__
solve = (1).__int__
solve = (1).__abs__
#solve = (1).__long__          # Python 2
solve = (1).__float__
solve = (-1).__neg__
solve = (-2).__invert__

"""Built-in str method"""
solve = "a".isalnum
solve = "a".isalpha
solve = "0".isdecimal
solve = "0".isdigit
solve = "True".isidentifier
solve = 'a'.islower
solve = "0".isnumeric
solve = "".isprintable
solve = " ".isspace
solve = "A".istitle
solve = "A".isupper
