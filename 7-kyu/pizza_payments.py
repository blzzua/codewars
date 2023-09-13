# https://www.codewars.com/kata/5b043e3886d0752685000009

def michael_pays(costs):
    if costs < 5:
        return round(costs, 2) 
    else:
        if costs/3 <= 10:
            return round(costs*2/3, 2)
        else:
            return round(costs-10, 2)
