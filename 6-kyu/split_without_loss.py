# https://www.codewars.com/kata/581951b3704cccfdf30000d2

def split_without_loss(inp_str, split_p):
    sep = split_p.replace("|", "")
    return [part for part in inp_str.replace(sep,split_p).split('|') if part]
