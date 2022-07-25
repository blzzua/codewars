# https://www.codewars.com/kata/557efeb04effce569d000022
import re
def make_acronym(phrase):
    print(phrase)
    if not isinstance(phrase, str):
        return "Not a string"
    if re.findall('[^a-z\s]', phrase, re.I):
        return 'Not letters'
    return "".join(word[0].upper() for word in phrase.split())
    

# clever
def make_acronym(phrase):
    try:
        return ''.join(word[0].upper() if word.isalpha() else 0 for word in phrase.split())
    except AttributeError:
        return 'Not a string'
    except TypeError:
        return 'Not letters'
