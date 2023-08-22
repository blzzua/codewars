# https://www.codewars.com/kata/59414b46d040b7b8f7000021

ingridient = {'a': 'beef', 'e': 'beef','u': 'beef','o': 'beef','u': 'beef','i': 'beef',
              't': 'tomato', 'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole', 's': 'salsa' 

def tacofy(word):
    print(word)
    middle = [ingridient.get(i) for i in word.lower() if i in ingridient]
    return ['shell'] + middle + ['shell']
