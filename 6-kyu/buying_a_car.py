# https://www.codewars.com/kata/554a44516729e4d80b000012

def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    price, m = 0, 0
    if start_price_old >= start_price_new:
        return [0,start_price_old - start_price_new]
    while price <= start_price_new:
        m = m + 1
        start_price_new = start_price_new - (start_price_new * (percent_loss_by_month/100))
        start_price_old = start_price_old - (start_price_old * (percent_loss_by_month/100))
        price = saving_per_month * m + start_price_old
        if m % 2:
            percent_loss_by_month = percent_loss_by_month + 0.5
    return [m, int(price - start_price_new + 0.5)]
