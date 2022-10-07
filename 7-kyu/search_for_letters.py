# https://www.codewars.com/kata/52dbae61ca039685460001ae

from string import ascii_lowercase
def change(st):
    return ''.join('1' if a in st.lower() else '0' for a in ascii_lowercase)

