# https://www.codewars.com/kata/59112b6424d75b2123000061

def concatenation_process(init):
    if len(init) == 1:
        return init[0]
    min_len_str_left = init[0]
    for s in init:
        if len(min_len_str_left) > len(s):
            min_len_str_left = s
    init.remove(min_len_str_left)
    min_len_str_right = init[0]
    for s in init:
        if len(min_len_str_right) >= len(s):
            min_len_str_right = s
    init.remove(min_len_str_right)
    init.append(min_len_str_left+min_len_str_right)
    return concatenation_process(init)
