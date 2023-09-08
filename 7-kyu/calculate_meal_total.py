# https://www.codewars.com/kata/58545549b45c01ccab00058c

def calculate_total(subtotal, tax, tip):
    return round(subtotal * ( 100 + tax ) / 100 + subtotal * (tip / 100 ), 2)
