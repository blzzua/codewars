# https://www.codewars.com/kata/584dc1b7766c2bb158000226

def chore_assignment(chores):
    l = len(chores)//2
    chores = sorted(chores)
    return sorted([x+y for x,y in zip(chores[:l], chores[l:][::-1])])
