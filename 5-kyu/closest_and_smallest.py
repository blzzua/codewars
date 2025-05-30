# https://www.codewars.com/kata/5868b2de442e3fb2bb000119
def closest(strng):
    weight = []
    for i, str_num in enumerate(strng.split()):
        w = sum(map(int, str_num))
        weight.append([w, i, int(str_num)])
    if weight == []:
        return []
    res = weight[0], weight[0]  # dummy 
    min_key = [99999999999,0,0] # initial [distance, weight_sum, index_sum]
    for i, w1 in enumerate(weight[:-1]):
        for j, w2 in enumerate(weight[i+1:]):
            distance = abs(w1[0] - w2[0])
            weight_sum = w1[0] + w2[0]
            index_sum = w1[1] + w2[1]
            
            if min_key >= [distance, weight_sum, index_sum]:
                res, min_key = ([w1, w2], [distance, weight_sum, index_sum])
    return sorted(res)
  
