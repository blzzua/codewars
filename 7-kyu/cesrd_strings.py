# https://www.codewars.com/kata/5ff6060ed14f4100106d8e6f

def uncensor(infected, discovered):
    return infected.replace("*","{}").format(*discovered)

