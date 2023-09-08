# https://www.codewars.com/kata/571d2e9eeed4a150d30011e7

scoremap = {'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}
   
def scoreboard(who_ate_what):
    return sorted([{'name': d['name'], 'score': sum(scoremap.get(k,0)*d[k] for k in d if k in scoremap)} for d in who_ate_what],
                  key=lambda d: (-d['score'], d['name']))
