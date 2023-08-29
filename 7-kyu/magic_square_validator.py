# https://www.codewars.com/kata/57be6a612eaf7cc3af000178

def is_magical(sq):
    const = sum(sq[:3])
    for j in range(3):
        if const != sum([sq[j*3+i] for i in range(3)]):
            q1=sum([sq[j*3+i] for i in range(3)])
            return False
    for j in range(3):
        if const != sum([sq[i*3+j] for i in range(3)]):
            q2=sum([sq[i*3+j] for i in range(3)])
            return False
    if const != sum(sq[i] for i in range(3)):
            q3=sum(sq[i] for i in range(3))
            return False
    if const != sum(sq[i*3+i] for i in range(3)):
            q4=sum(sq[i*3+i] for i in range(3))
            return False
    return True
