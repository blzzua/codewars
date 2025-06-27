# https://www.codewars.com/kata/58d76854024c72c3e20000de

def reverse_alternate(st):
    while st != st.replace('  ',' '):
        st = st.replace('  ',' ')
    res = []
    for i, word in enumerate(st.split(' ')):
        if word:
            if i % 2 ==1:
                res.append(word[::-1])
            else:
                res.append(word)
    return ' '.join(res)
