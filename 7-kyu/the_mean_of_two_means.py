# https://www.codewars.com/kata/583df40bf30065fa9900010c

def get_mean(arr,x,y):
    n = len(arr)
    if x > n or y > n or x <= 1 or y <= 1:
        return -1
    x_arr = arr[:x]
    y_arr = arr[-y:]
    mean_x = sum(x_arr)/x
    mean_y = sum(y_arr)/y
    return (mean_x + mean_y)/2
