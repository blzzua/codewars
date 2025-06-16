# https://www.codewars.com/kata/57de02e2f5ec16bda100074f

def three_wishes(parcel, wish1, wish2, wish3):
    wishes = []
    for wish in wish1, wish2, wish3:
        wish = wish[7:]
        cnt,_,what = wish.partition(' ')
        cnt = int(cnt)
        if cnt > 1:
            wish = what[0:-1]
        else:
            wish = what
        if wish == 'wish' or wish == 'wishe': # greedy algorythm
            return [] 
        wishes.extend( [wish] * cnt )
    # expand parcel
    for i, p_wish in enumerate(parcel):
        if p_wish in wishes:
            parcel.insert(i,wishes.pop(wishes.index(p_wish)))
    if wishes:
        parcel.extend(wishes)
    return parcel
