# https://www.codewars.com/kata/5296455e4fe0cdf2e000059f

def calculate(num1, operation, num2): 
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/' and num2 != 0:
        return num1 / num2


