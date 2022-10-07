# https://www.codewars.com/kata/62cb487e43b37a5829ab5752

from preloaded import FILTERS
import re


def is_valid(query: str) -> bool:
    return bool(re.match(r'^([^:]+)?\b(('+'|'.join(FILTERS)+'):([^:]+))*$', query))

