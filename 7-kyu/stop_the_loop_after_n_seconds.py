# https://www.codewars.com/kata/5a147735ffe75f1c75000199

import time

def increment_loop(n):
    timeout = time.time() + n
    i=0
    while True and time.time() < timeout:
        i+=1
    return i
    

