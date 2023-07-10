# https://www.codewars.com/kata/5706be574f2c297a7b00060d

soil_map = {'Barely used': 0.1, 'Seen a few high kicks': 0.25, 'Blood stained': 0.30, 'Heavily soiled': 0.50}

def price(start, soil, age):
    try:
        for i in range(age):
            start += start*soil_map[soil]
        return '${0:.2f}'.format(round(start,2))
    except (TypeError, KeyError) as e:
        return 'Chuck is bottomless!'
