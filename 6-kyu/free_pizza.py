# https://www.codewars.com/kata/595910299197d929a10005ae

def pizza_rewards(customers, min_orders, min_price):
    res = set()
    for customer, orders in customers.items():
        cnt_expensive_pizzas = 0
        for order_price in orders:
            if order_price >= min_price:
                cnt_expensive_pizzas += 1
        if cnt_expensive_pizzas >= min_orders:
            res.add(customer)
    return res
  
