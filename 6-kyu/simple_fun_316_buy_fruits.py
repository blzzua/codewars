# https://www.codewars.com/kata/5934c24ed953868340000014

from collections import Counter
def buy_fruits(price_labels, fruits_list):
    fr_counter = Counter(fruits_list)
    fi = sorted(fr_counter.values())
    expensive = sum(c*p for c,p in zip(sorted(fi, reverse=True), sorted(price_labels,reverse=True)))
    cheap = sum(c*p for c,p in zip(sorted(fi, reverse=True), sorted(price_labels,reverse=False)))
    return cheap,expensive

