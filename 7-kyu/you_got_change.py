# https://www.codewars.com/kata/5966f6343c0702d1dc00004c

def give_change(amount): 
    nominals = [1,5,10,20,50,100][::-1]
    res = []
    for banknote in nominals:
        print(amount,banknote, divmod(amount,banknote))
        cnt, amount = divmod(amount,banknote)
        res.append(cnt)
    return tuple(res[::-1])


