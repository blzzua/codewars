# https://www.codewars.com/kata/5827acd5f524dd029d0005a4

def is_ruby_coming(lst): 
    return any([d['language'] for d in lst if d['language'] == "Ruby"])

