# https://www.codewars.com/kata/587fb57e12fc6eadf200009b

import hashlib
def to_sha256(s):
    hasher = hashlib.sha256()
    hasher.update(s.encode('utf-8'))
    return hasher.hexdigest()

return hashlib.sha256(s.encode('utf-8')).hexdigest()
