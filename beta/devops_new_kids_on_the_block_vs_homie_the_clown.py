# https://www.codewars.com/kata/58b497914c5d0af407000049

def nkotb_vs_homie(requirements):
    res = []
    monitoring, automation, deployment, cloud, microservices = [len(r) for r in requirements]
    for group in requirements:
        for r in group:
            r = r.replace('We need ','').replace(' now!', '').capitalize()
            res.append(f'{r}! Homie dont play that!')
    return res + [f'{monitoring} monitoring objections, {automation} automation, {deployment} deployment pipeline, {cloud} cloud, and {microservices} microservices.']
