# https://www.codewars.com/kata/59ffe8bbffe75f6d94000016

from functools import wraps

def count_calls(func):
    @wraps(func)
    def internal(*args, **kwargs):
        if not hasattr(internal, 'call_count'):
            internal.call_count = 0
        internal.call_count += 1
        return func(*args, **kwargs)
        
    internal.call_count = 0
    return internal

