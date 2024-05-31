# https://www.codewars.com/kata/5f25f475420f1b002412bb1f

al = 'abcdefghijklmnopqrstuvwxyz'
def find_the_number_plate(customer_id):
    rest, num = divmod(customer_id, 999)
    rest, a = divmod(rest, 26)
    c, b = divmod(rest, 26)
    return f'{al[a]}{al[b]}{al[c]}{num+1:03d}'
