# https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc

def split_by_value(k, elements):
    return list(filter(lambda x: x<k, elements)) + list(filter(lambda x: x>=k, elements))
    
# clever sorted(elements, key=lambda x: x>=k)
