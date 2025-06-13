# https://www.codewars.com/kata/56a32dd6e4f4748cc3000006

import statistics
import re

def mean(town, s):
    for line in s.split('\n'):
        if line.startswith(town+':'):
            data = map(float, re.split('[, ]', line.partition(':')[2])[1::2])
            return  round(statistics.mean(data),2)
    return -1

def variance(town, s):
    for line in s.split('\n'):
        if line.startswith(town+':'):
            data = list(map(float, re.split('[, ]', line.partition(':')[2])[1::2]))
            m = statistics.mean(data)
            res = sum([(d - m)**2 for d in data]) / len(data)
            return res
    return -1

