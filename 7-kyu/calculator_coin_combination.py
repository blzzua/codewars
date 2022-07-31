# https://www.codewars.com/kata/564d0490e96393fc5c000029

def coin_combo(cents):
    nominals = [1,5,10,25]
    for i in range(len(nominals)-1,-1,-1):
        nominals[i], cents = divmod(cents, nominals[i])
    return nominals
