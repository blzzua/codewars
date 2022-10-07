# https://www.codewars.com/kata/594adadee075005308000122

def even_and_odd(n): 
    ne, no = [], []
    for d in str(n):
        [ne,no][int(d)%2].append(d)
    ne = int(''.join(ne)) if ne else 0
    no = int(''.join(no)) if no else 0
    #tuple(map(int,map(''.join,(ne, no))))
    return (ne,no)
    

