https://www.codewars.com/kata/61c78b57ee4be50035d28d42

def merge_strings(first, second):
    for i in range(min(len(first),len(second)) , -1, -1):
        if first[-i:] == second[:i]:
            return first + second[i:]
    else:
        return first + second
