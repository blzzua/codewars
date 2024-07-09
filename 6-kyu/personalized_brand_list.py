# https://www.codewars.com/kata/57cb12aa40e3020bb4001d2e

from collections import Counter
def sorted_brands(history):
    need_data = [item['brand'] for item in history]
    # need_data = [item['brand'] for item in history]
    cnt = Counter(need_data)
    unsorted = []
    for brand in cnt:
        ordinal = need_data.index(brand)
        unsorted.append((-cnt[brand], ordinal, brand))
    return [brand for cnt, ordinal, brand in sorted(unsorted)]
