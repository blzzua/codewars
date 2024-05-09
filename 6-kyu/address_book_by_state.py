# https://www.codewars.com/kata/59d0ee709f0cbcf65400003b

STATES = {  'AZ': 'Arizona',
            'CA': 'California',
            'ID': 'Idaho',
            'IN': 'Indiana',
            'MA': 'Massachusetts',
            'OK': 'Oklahoma',
            'PA': 'Pennsylvania',
            'VA': 'Virginia'}

from collections import defaultdict
def by_state(st):
    res = defaultdict(list)
    for row in st.rstrip('\n').split('\n'):
        addr = row[:-3]
        state = row[-2:]
        res[state].append(''.join(addr.split(',')) + ' ' + STATES[state])
    ret = []
    for state in sorted(res.keys()):
        ret.append(' '+ STATES[state])
        for row in sorted(res[state]):
            ret.append('..... ' + row)
    return '\r\n'.join(ret)[1:]
