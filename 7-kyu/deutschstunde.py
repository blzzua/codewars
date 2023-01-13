# https://www.codewars.com/kata/552cd8624a414ec2b2000086

def der_die_das(wort):
    wc = sum(wort.lower().count(w)  for w in 'aeiouäöü')
    if wc < 2:
        return f'das {wort}'
    if wc < 4:
        return f'die {wort}'
    return f'der {wort}'
