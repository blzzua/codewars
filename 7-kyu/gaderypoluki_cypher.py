# https://www.codewars.com/kata/592a6ad46d6c5a62b600003f

def encode(message, code="GADERYPOLUKIgaderypoluki"):
    edoc = ''.join( b+a  for a,b in zip(code[::2],code[1::2]))
    return message.translate(message.maketrans(code, edoc))

decode = encode 
