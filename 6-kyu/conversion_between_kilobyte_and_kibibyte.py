# https://www.codewars.com/kata/5a115ff080171f9651000046

def format_size(size):
    s_string = f'{size:.3f}'.rstrip('0')
    if s_string[-1] == '.': 
        s_string = f'{s_string}0'
    return s_string


def memorysize_conversion(memorysize):
    decimal = ['kB', 'MB', 'GB', 'TB']
    binary = ['KiB', 'MiB', 'GiB', 'TiB']
    size_str, unit = memorysize.split(' ')
    size = float(size_str)
    if unit in decimal:
        size = size / (1.024**(decimal.index(unit)+1))
        target_unit = binary[decimal.index(unit)]
                
    if unit in binary:
        size *= 1.024**(binary.index(unit)+1)
        target_unit = decimal[binary.index(unit)]

    return f'{format_size(size)} {target_unit}'
