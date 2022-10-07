# https://www.codewars.com/kata/5808c8eff0ed4210de000008

def part(arr):
    cnt = sum(w in ['Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad'] for w in arr)
    if cnt:
        return 'Mine\'s a Pint' + '!' * cnt
    else:
        return 'Lynn, I\'ve pierced my foot on a spike!!'

