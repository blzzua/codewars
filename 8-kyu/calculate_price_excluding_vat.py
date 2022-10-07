# https://www.codewars.com/kata/5890d8bc9f0f422cf200006b

def excluding_vat_price(price):
    try:
        return round(price * 20 / 23, 2)
    except TypeError:
        return -1


