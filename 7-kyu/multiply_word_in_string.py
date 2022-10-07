# https://www.codewars.com/kata/5ace2d9f307eb29430000092

def modify_multiply(st, loc, num):
    return '-'.join(st.split()[loc] for _ in range(num))

