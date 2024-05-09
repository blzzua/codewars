# https://www.codewars.com/kata/58b3c2bd917a5caec0000017

def sum_groups(arr, is_cummulated=True):
    while is_cummulated:
        res = []
        parity = arr[0] % 2
        cur_sum = 0
        is_started = True
        is_cummulated = False
        for i in arr:
            if  i % 2 == parity:
                cur_sum += i
                if is_started:
                    is_started = False
                else:
                    is_cummulated = True
            else:
                res.append(cur_sum)
                cur_sum = i
                parity = 1 - parity
        res.append(cur_sum)
        arr = res
    return len(arr)
