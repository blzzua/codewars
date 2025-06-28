# https://www.codewars.com/kata/58c61a1e8a452631c5000003

def counterfeit_dollar(results):
    true_coins = set()
    for res in results:
        left, right, status = res.split(' ')
        if status == 'even':
            [true_coins.add(c) for c in left + right]
        else:
            sus_left, sus_right, sus_status = res.split(' ')
    
    sus_left = set(sus_left).difference(true_coins)
    sus_right = set(sus_right).difference(true_coins)
    if len(sus_left) + len(sus_right) > 1:
        return '???'
    if (sus_status == 'up' and sus_right) or (sus_status == 'down' and sus_left):
        weight = 'light'
        letter = (sus_right.union(sus_left)).pop()
    if (sus_status == 'down' and sus_right) or (sus_status == 'up' and sus_left):
        weight = 'heavy'
        letter = (sus_right.union(sus_left)).pop()
    try:
        return f'{letter} is the counterfeit coin and it is {weight}.'
    except UnboundLocalError as e:
        return '???'

