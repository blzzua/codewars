# https://www.codewars.com/kata/53697be005f803751e0015aa

ENCMAP = str.maketrans({'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'})
DECMAP = str.maketrans({'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'})

def encode(st):
    return st.translate(ENCMAP)
    
def decode(st):
    return st.translate(DECMAP)
