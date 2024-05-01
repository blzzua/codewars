# https://www.codewars.com/kata/5d7091aa7bf8d0001200c133

data = """
|  ###  |       |  ###  |  ###  |       |  ###  |  ###  |  ###  |  ###  |  ###  |       |
| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |       |
| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |       |
| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |       |
|       |       |  ###  |  ###  |  ###  |  ###  |  ###  |       |  ###  |  ###  |       |
| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |       |
| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |       |
| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |       |
|  ###  |       |  ###  |  ###  |       |  ###  |  ###  |       |  ###  |  ###  |       |
"""
I = '|' # separator
DISPLAY_LEN = 6
intermediate = [line.split(I)[1:-1] for line in data.strip().split('\n')]
zipped_numbers = [v for v in zip(*intermediate)]

def segment_display(num):
    symbols = [10 if char == ' ' else int(char) for char in str(num).rjust(DISPLAY_LEN)]
    res = [ I + I.join(line) + I for line in zip(*[zipped_numbers[s] for s in symbols])]
    return '\n'.join(res)
