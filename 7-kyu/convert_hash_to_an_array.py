# https://www.codewars.com/kata/59557b2a6e595316ab000046

def convert_hash_to_array(hash):
    return sorted([list(pair) for pair in hash.items()])

