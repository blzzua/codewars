# https://www.codewars.com/kata/61db0b0d5b4a78000ef34d1f

def bus_animation(bus_size, bus_speed, frame_count, frame_size):
    head = ['_____', '| |  \\  ', '|_|___\\ ', '| |    \\', "--(o)--'"]
    tail = [' ___', '|   ', '|___', '|   ', '`---']
    body = ['_____', '|    ', '|____', '     ', '-----']
    separator = ' '*frame_size+'\n' + '-'*frame_size
    bus = [t + (b*bus_size) + h for h,b,t in zip(head, body, tail)]
    bus[-1] = '`--(o)(o)' + bus[-1][9:] # wheels
    res = []
    for frame in range(frame_count):
        for bus_line in bus:
            res.append(((bus_speed * frame * ' ') + bus_line + (' ' * frame_size))[:frame_size])
        if (frame_count - frame) != 1:
            res.append(separator)
    return '\n'.join(res)
