# https://www.codewars.com/kata/62c4ad0e86f0166ec7bb8485
# Number Pyramid
# Image a number pyramid starts with 1, and the numbers increasing by 1.
# For example, when the pyramid has 3 levels:
#   1
#  2 3
# 4 5 6
# And the sum of three corners are:
# 1 + 4 + 6 = 11
# The length of your code should be less or equal to 35.

# common soultion: 
# https://en.wikipedia.org/wiki/Triangular_number
# for n > 2:  1 + T(n-1) + 1 + Tn ; where T(n) = C(n+1,2) = n*(n+1)/2 => n*(n+1)/2+(n+1)*(n+2)/2+2 = n*n+2
# but for corner cases:
# n == 1 : 1
# n == 0 : 0 


# limited 35 to characters (declare function using lambda-notation):
sum_corners=lambda n:n*n+2*(n>1)
sum_corners=lambda n:[n,n*n+2][n>1]
