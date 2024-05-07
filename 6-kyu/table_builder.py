# https://www.codewars.com/kata/5ff369c8ee41be0021770fee

def build_table(inp, style):
    if inp == []:
        return ''
    max_widths = [max(w) for w in zip(*[[len(cell) for cell in line] for line in inp])]
    res = ['']
    def h_align(text,align,width):
        if align == 'mid':
             #return str(text[::-1]).center(width)[::-1]
            if len(text) % 2:
                return str(text).center(width)
            else:
                return str(text + ' ').center(width+1)[:-1]
        if align == 'left':
             return str(text) + max(0,width - len(text)) * ' '
        if align == 'right':
             return ' ' * max(0,width - len(text)) + str(text)
            
    for row in inp:
        row_cells = [style.sep_hi * style.off_min + \
                    h_align(cell, style.align, width).replace(' ', style.sep_hi) + \
                     style.sep_hi * style.off_min \
                            for cell, width in zip(row, max_widths)]
        row_str = style.sep_ve + style.sep_vi.join(row_cells) + style.sep_ve
        res.append(row_str)
    res[0] = len(res[1]) * style.sep_he
    return '\n'.join(res)
