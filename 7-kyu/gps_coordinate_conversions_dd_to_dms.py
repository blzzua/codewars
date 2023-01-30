# https://www.codewars.com/kata/5a72fd224a6b3463b00000a0

def convert_to_dms(dd_lat, dd_lon):
    
    deg = int(abs(dd_lat))
    rest = abs(dd_lat) - deg
    min = int(rest * 60)
    sec = int( (rest - min/60) * 3600)
    sec += round( (rest  - min / 60) * 3600 - sec, 3)
    lat_char = 'S' if dd_lat < 0 else 'N'
    dms_lat = '{0:03d}*{1:02d}\'{2:06.3f}"{3}'.format(deg, min, sec, lat_char)

    deg = int(abs(dd_lon))
    rest = abs(dd_lon) - deg
    min = int(rest * 60)
    sec = int( (rest - min/60) * 3600)
    sec += round( (rest  - min / 60) * 3600 - sec, 3)
    lon_char = 'W' if dd_lon < 0 else 'E'
    dms_lon = '{0:03d}*{1:02d}\'{2:06.3f}"{3}'.format(deg, min, sec, lon_char)

    return dms_lat, dms_lon
