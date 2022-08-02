# https://www.codewars.com/kata/564f3d49a06556d27c000077

def pattern(n):
    return '\n'.join(' '*i + (' ' + str((i+1)%10))*(n-i) for i in range(n))

## best practices
def pattern(n):
    triangle = ""
    for i in range(n):
        triangle += " "*(i + 1)
        triangle += " ".join(str((i + 1)%10)*(n - i))
        if i < n - 1:
            triangle += "\n"
    return triangle
