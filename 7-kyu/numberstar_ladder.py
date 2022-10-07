# https://www.codewars.com/kata/5631213916d70a0979000066

def pattern(n):
    return '\n'.join((['1'] + ['1'+ '*'*i + str(i+1) for i in range(1,n)]))
    


