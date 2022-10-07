# https://www.codewars.com/kata/52a723508a4d96c6c90005ba

def sing():
    res = []
    for i in range(99, 2, -1):
        res.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        res.append(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
    res.append(f"2 bottles of beer on the wall, 2 bottles of beer.")
    res.append(f"Take one down and pass it around, 1 bottle of beer on the wall.")
    res.append(f"1 bottle of beer on the wall, 1 bottle of beer.")
    res.append(f"Take one down and pass it around, no more bottles of beer on the wall.")
    res.append(f"No more bottles of beer on the wall, no more bottles of beer.")
    res.append(f"Go to the store and buy some more, 99 bottles of beer on the wall.")
    return res

