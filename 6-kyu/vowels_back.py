# https://www.codewars.com/kata/57cfd92c05c1864df2001563

def vowel_back(st):
    return st.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'vkbaafpqistuvwnyzabtpvfghi'))
