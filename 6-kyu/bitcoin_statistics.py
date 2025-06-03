# https://www.codewars.com/kata/5a7f6b615084d75df6000032

def get_min_avg_max(discard, data):
    totalmax_ = 0
    totalmin_ = 999999999999999
    totalsum_ = 0
    totallen_ = 0
    res = []
    for line in data:
        line = line[discard::][::-1][discard::]
        max_, min_, sum_, len_ = max(line),min(line),sum(line),len(line)
        res.append( (min_, sum_/len_, max_) )
        totalmax_ = max([totalmax_, max_])
        totalmin_ = min([totalmin_, min_])
        totalsum_ += sum_
        totallen_ += len_
    res.append( (totalmin_, totalsum_/totallen_ ,totalmax_) )
    print(discard, data, res)
    return res

