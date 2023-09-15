# https://www.codewars.com/kata/609ccb2091b67a00076f6731

def encrypt(st, encryption_dict):
    return st.translate(str.maketrans(encryption_dict))
    
def decrypt(st, encryption_dict):
    dec_dict = dict([(v,k) for k,v  in sorted(encryption_dict.items(), key = lambda x: len(x[1]), reverse = True )])
    res = []
    for _ in st:
        for k in dec_dict:
            if st.startswith(k):
                res.append(k)
                st = st.replace(k,'',1)
        if st == '':
            break
    return ''.join(map(dec_dict.get, res))
