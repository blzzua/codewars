# https://www.codewars.com/kata/57e6bcbd684e570c6700021c

import re

colormap = {'gold': 'ForestGreen', 'khaki': 'LimeGreen', 'lemonchiffon': 'PaleGreen', 
'lightgoldenrodyellow': 'SpringGreen', 'lightyellow': 'MintCream', 'palegoldenrod': 'LightGreen', 'yellow': 'Lime'}

def yellow_be_gone(color_name_or_code):
    if re.fullmatch(r"#([a-fA-F0-9]{6})", color_name_or_code):
        r, g, b = color_name_or_code[1:3], color_name_or_code[3:5], color_name_or_code[5:7]
        if r > b and g > b:
            if r > g:
                return f"#{b}{r}{g}"
            else:
                return f"#{b}{g}{r}"
    # else colormap
    return colormap.get(color_name_or_code.lower(), color_name_or_code)
