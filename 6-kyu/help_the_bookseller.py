# https://www.codewars.com/kata/54dc6f5a224c26032800005c

def stock_list(stocklist, categories):
    if stocklist == []:
        return ''
    cat_num = {category: 0 for category in categories }
    for book_line in stocklist:
        book_code, num = book_line.split(' ')
        if book_code[0] in cat_num:
            cat_num[book_code[0]] += int(num)
    res = ' - '.join(f'({category} : {number})' for category, number in cat_num.items())
    return res

