# https://www.codewars.com/kata/53e248c9af0d91a45b000e71

import os

def mkdirp(*directories):
    path = '/'
    for dir in directories:
        path = os.path.join(path, dir)
        if os.path.exists(path) and os.path.isdir(path):
            continue
        elif not os.path.exists(path):
            os.mkdir(path)
