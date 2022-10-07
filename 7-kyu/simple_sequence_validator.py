# https://www.codewars.com/kata/553f01db29490a69ff000049

def validate_sequence(s):
    return all(a-b == s[0]-s[1] for a,b in zip(s,s[1::]))

