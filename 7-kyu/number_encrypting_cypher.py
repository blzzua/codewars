# https://www.codewars.com/kata/57aa3927e298a757820000a8
def cypher(string):
    tr = str.maketrans({k:v for k,v in zip('IREASGTBO'+'lzeasbtgo','123456780'+'123456790')})
    return string.translate(tr)
