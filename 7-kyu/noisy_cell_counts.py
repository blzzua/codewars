# https://www.codewars.com/kata/63ebadc7879f2500315fa07e

def cleaned_counts(data):
    res = [data[0]]
    for i in data[1:]:
        res.append(max(i,res[-1]))
    return res

# clever itertools.accumulate(data, max)
