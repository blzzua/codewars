# https://www.codewars.com/kata/6400c3ebf4a0b796602988a6

w_map = {'R': 25, 'B': 20, 'Y': 15, 'G': 10, 'W': 5,  'r': 2.5, 'b': 2, 'y': 1.5, 'g': 1, 'w': 0.5} 
w_rev = {v:k for k,v in w_map.items()} 
bar = 20
w_list = list(w_map.values())

def greedy_backpack(target_weight): # common problem
    weight_list = sorted(w_list, reverse=True)
    backpack = {}
    for weight in weight_list:
        while target_weight >= weight:
            target_weight -= weight
            backpack[weight] = backpack.get(weight, 0) + 1
    return backpack

def load_barbell(weight):
    target = (weight - bar - 2*2.5) / 2
    w_dict = greedy_backpack(target)
    c1 = ''.join([w_rev.get(w)*cnt for w, cnt in w_dict.items() if w >= 2.5] + ['c'] + [w_rev.get(w)*cnt for w, cnt in w_dict.items() if w < 2.5])
    c2 = c1[::-1]
    c2 = c2.zfill(10).replace('0','-')
    c1 = c2[::-1]
    c_bar = '-'*20
    return c2 + c_bar + c1
