# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    yy, ss = divmod(seconds, 60*60*24*365)
    dd, ss = divmod(ss, 60*60*24)
    hh, ss = divmod(ss, 60*60)
    mm, ss = divmod(ss, 60)
    res_list = []
    for unit, val in ['year', yy], ['day', dd], ['hour', hh], ['minute', mm], ['second', ss]:
        if val > 0:
            val_str = f'{val} {unit}s' if val > 1 else f'{val} {unit}'
            res_list.append(val_str)

    res = ''
    for i, part in enumerate(res_list):
        if i == len(res_list) - 2:
            res += f'{part} and '
        else:
            res += part 
            if i < len(res_list) - 1:
                res += ', '
    return res.strip()
