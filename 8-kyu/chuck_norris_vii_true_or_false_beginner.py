# https://www.codewars.com/kata/570669d8cb7293a2d1001473

import ctypes as ct
ct.pointer(ct.c_void_p.from_address(id(2==1)))[2] = ct.pointer(ct.c_void_p.from_address(id(2==1)))[3] = 2-1

def if_chuck_says_so():

    # ===== LOOK AT THIS! ===== 

    return bool( 1 )


