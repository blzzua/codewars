# https://www.codewars.com/kata/587b6a5e8726476f9b0000e7

def rot_energies(B, Jmin, Jmax):
    if Jmin > Jmax or B < 0:
        return []
    return [ B * i * (i + 1) for i in range(Jmin, Jmax+1)]
