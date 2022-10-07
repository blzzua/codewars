# https://www.codewars.com/kata/5b6375f707a2664ada00002a

def who_is_online(friends):
    res = {}
    for p in friends:
        if p.get('status') == 'online' and p.get('last_activity') > 10:
            p['status'] = 'away'
        if p.get('status') in res:
            res[p.get('status')].append(p.get('username'))
        else:
            res[p.get('status')] = [p.get('username')]
    return res
    

