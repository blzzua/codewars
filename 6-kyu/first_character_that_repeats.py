# https://www.codewars.com/kata/54f9f4d7c41722304e000bbb

def first_dup(s):
    cnt = {}
    cand = set()
    for i, char in enumerate(s):
        if char not in cnt:
            cnt[char] = i
        else:
            cand.add(char)
    if cand:
        return min([(index, chr) for chr, index in cnt.items() if chr in cand])[1]
    else:
        return None
