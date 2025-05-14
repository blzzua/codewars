# https://www.codewars.com/kata/5ab3be5f6a176bef4e00012d

def hexdump(data):
    res = []
    for line_num in range((len(data)+15)//16):
        start = line_num*16
        end = start+16 if start+16 < len(data) else len(data)
        line = data[start:end]
        hex_presentation = ([str.format('{0:02x}', char) for char in line] + ['  '] * 16)[:16]
        hex_str = ' '.join(hex_presentation)
        chr_presentation = [str.format('{0}', chr(char) if 32 <= char <= 126 else '.'  ) for char in line]
        chr_str = ''.join(chr_presentation)
        line_num_str = str.format('{0:08x}', line_num*16)
        line_str = f'{line_num_str}: {hex_str}  {chr_str}'
        res.append(line_str)
    return '\n'.join(res)

def dehex(text):
    res = []
    for line in text.split('\n'):
        line = line.strip(' ')
        hex = line[10:57].strip(' ') # 57 = 10+16+15+16
        res.extend([int(ch,16) for ch in hex.split(' ')])
    return bytes(res)

