# https://www.codewars.com/kata/586a1af1c66d18ad81000134

def driver(data):

    name = (data[2]+'99999')[:5].upper()
    dd = data[3][-2]
    month = ('Zero', 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
    m = month.index(data[3][3:6])
    if data[4] == 'F':
        m += 50
    m = str(m).zfill(2)
    day = data[3][0:2]
    year = data[3][-1]
    if data[1] == '':
        i = data[0][0] + '9'
    else:
        i = data[0][0] + data[1][0]
    return name + dd + m + day + year + i + '9AA'

