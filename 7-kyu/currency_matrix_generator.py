# https://www.codewars.com/kata/57bec3bc5640aa5f3f00003e

ccy = ["EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]

def generate_currency_matrix(currency):
    return [''.join(sorted((currency,p),key=ccy.index)) for p in ccy if p != currency]
