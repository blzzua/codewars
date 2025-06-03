# https://www.codewars.com/kata/57fe7ea808d102a2ba000edd

def pluralize(word):
    if word.endswith('ch') or  word.endswith('sh') or  word.endswith('x') or  word.endswith('z') or  word.endswith('s'):
        return word + 'es'
    if word.endswith('y'):
        if len(word) > 1 and word[-2] in 'aueiou':
            return word + 's'
        else:
            return word[:-1] + 'ies'
    return word + 's'

