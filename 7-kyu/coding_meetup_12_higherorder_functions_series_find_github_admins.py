# https://www.codewars.com/kata/582dace555a1f4d859000058

def find_admin(lst, lang): 
    return [o for o in lst if o['language'] == lang and o['githubAdmin'] == 'yes']

