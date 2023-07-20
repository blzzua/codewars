# https://www.codewars.com/kata/5a39724945ddce2223000800

def total_amount_visible(top_num, num_of_sides):
    return ((num_of_sides+1) * num_of_sides//2) - ((num_of_sides+1) - top_num )
