# https://www.codewars.com/kata/543e8390386034b63b001f31

from collections import defaultdict

def get_char_count(strng: str) -> dict[int, list[str]]:
    s = strng.lower()
    sfd = {c: s.count(c) for c in s if c.isalnum()} # strng filtered dict
    res = defaultdict(list)
    for letter,cnt in sfd.items():
        res[cnt].append(letter)

    return {cnt: sorted(res[cnt]) for cnt in sorted(res, reverse=True)}

