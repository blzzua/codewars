# https://www.codewars.com/kata/5822b65bb81f702016000026

def linux_type(f):
    return {'-': 'file', 'd': 'directory', 'l': 'symlink', 'c': 'character_file', 'b': 'block_file', 'p': 'pipe', 's': 'socket', 'D': 'door'}[f[0]]

