# https://www.codewars.com/kata/57280481e8118511f7000ffa

def split_and_merge(string, separator):
    return ' '.join([separator.join(word) for word in string.split(' ')])

