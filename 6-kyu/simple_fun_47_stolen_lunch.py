# https://www.codewars.com/kata/58884a65f06a3d3bef000049

def stolen_lunch(note):
    d = "0123456789"
    l = "abcdefghij"
    trans = str.maketrans(d + l, l + d)
    return note.translate(trans)

