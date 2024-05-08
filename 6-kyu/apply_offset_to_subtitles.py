# https://www.codewars.com/kata/5e454bf176551c002ee36486

def ts2ms(TS):
    hms, ms=TS.split(',')
    h,m,s = hms.split(':')
    h,m,s,ms = map(int,(h,m,s,ms))
    total_ms = sum((h*1000*3600,m*1000*60,s*1000,ms))
    return total_ms

def ms2ts(total_ms):
    h, rest = divmod(total_ms,3600*1000)
    m, rest = divmod(rest,60*1000)
    s, ms = divmod(rest,1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'

def subs_offset_apply(string, offset):
    ts1, _sep1, ts2_and_text = string.partition(' --> ')
    ts2, _sep2, text = ts2_and_text.partition(' ')
    
    ms1, ms2 = ts2ms(ts1), ts2ms(ts2)
    border_min, border_max  = ts2ms('00:00:00,000'), ts2ms('99:59:59,999')
    if (ms1 + offset < border_min) or (ms2 + offset > border_max):
        return 'Invalid offset'
    
    ms1s = ms2ts(ms1 + offset)
    ms2s = ms2ts(ms2 + offset)
    return f'{ms1s}{_sep1}{ms2s}{_sep2}{text}'
