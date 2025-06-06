# https://www.codewars.com/kata/59de1e2fe50813a046000124

def is_valid_phone(phone):
    if len(phone) == len("+1-503-555-0090"):
        if (phone[0:3] == '+1-' and phone[6] == '-' == phone[10] and (phone[3:6] + phone[7:10] + phone[11:]).isnumeric()):
            return True
    else:
        return False

def is_valid_version(version):
    if version.count('.') != 1:
        return False
    a,b = version.split('.')
    if not(a.isnumeric() and b.isnumeric()):
        return False
    return True

def change(s, prog, version):
    print(s, '\n', prog, '\n', version)
    res = {}
    for line in s.split('\n'):
        k, _, v = line.partition(': ')
        res[k] = v
    res['Author'] = 'g964'
    res['Program title'] = prog
    if is_valid_phone(res['Phone']):
        res['Phone'] = '+1-503-555-0090'
    else:
        return 'ERROR: VERSION or PHONE'
    if is_valid_version(res['Version']):
        if res['Version'] != '2.0':
            res['Version'] = version
    else:
        return 'ERROR: VERSION or PHONE'

    program = res['Program title']
    author = res['Author']
    phone = res['Phone']
    version = res['Version']
    return f'Program: {program} Author: {author} Phone: {phone} Date: 2019-01-01 Version: {version}'
