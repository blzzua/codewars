# https://www.codewars.com/kata/57ab2d6072292dbf7c000039

def correct_polish_letters(st):
    return st.translate(str.maketrans('ąćęłńóśźż', 'acelnoszz'))

