# https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763

def show_sequence(n):
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return '0=0'
    else:
        s = sum(i for i in range(n+1))
        return '+'.join(str(i) for i in range(n+1))+f' = {s}'

