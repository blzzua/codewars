# https://www.codewars.com/kata/60d20fe1820f1b004188ceed
# [Code Golf] A Triangle?
# 
# Given three sides a, b and c, determine if a triangle can be built out of them.
# Your code can be up to 40 characters long.



# nominal solution:
def triangle(a, b, c):
    if c >= a and c >= b and a + b <= c :
        return False  
    elif a >= b and a >= c and  b + c <= a:
        return False
    elif b >= c and b >= a and c + a <= b:
        return False
    else:
        return True


# my solution longer than 40 chars
triangle=lambda *t:all(sum(t)-l>l for l in t)

# yet another clever
triangle=lambda a,b,c:b+c>a>c-b>-a

# shortest:
triangle=lambda*a:2*max(a)<sum(a)
triangle=lambda*a:max(a)<sum(a)/2
