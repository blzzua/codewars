# https://www.codewars.com/kata/5a995c2aba1bb57f660001fd

def scrolling_text(text):
    text = text.upper()
    return [text[i:] + text[:i] for i,_ in enumerate(text)]

