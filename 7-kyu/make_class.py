# https://www.codewars.com/kata/5d774cfde98179002a7cb3c8

import dataclasses
def make_class(*args):
    return dataclasses.make_dataclass('Animal', args)
