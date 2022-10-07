# https://www.codewars.com/kata/5815f7e789063238b30001aa

def redistribute_wealth(wealth):
    avg = sum(wealth)/len(wealth)
    if all(w == avg for w in wealth):
        return None
    
    if int(avg) == avg:
        avg = int(avg)

    for i, _  in enumerate(wealth):
        wealth[i] = avg


