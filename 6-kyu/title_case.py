# https://www.codewars.com/kata/5202ef17a402dd033c000009

def title_case(title, minor_words=''):
    mw_list = minor_words.lower().split()
    res = []
    for word in title.split():
        if word.lower() in mw_list:
            word = word.lower()
        else:
            word = word.capitalize()
        res.append(word)
    if res:
        res[0] = res[0].capitalize()
    return ' '.join(res)
