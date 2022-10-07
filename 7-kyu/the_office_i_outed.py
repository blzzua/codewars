# https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1

def outed(meet, boss):
    if (sum(meet.values()) + meet[boss]) / len(meet) > 5:
        return 'Nice Work Champ!'
    else:
        return 'Get Out Now!'

