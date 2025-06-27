# https://www.codewars.com/kata/547f601b4a437a2048000981

def find_duplicates(emp):
    uniq = []
    duplicates = []
    seen = set()
    for i in emp:
        if i in seen:
            duplicates.append(i)
        else:
            uniq.append(i)
            seen.add(i)
    emp.clear()
    emp.extend(uniq)
    return duplicates
