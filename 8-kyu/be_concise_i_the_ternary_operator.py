# https://www.codewars.com/kata/56f3f6a82010832b02000f38

def describe_age(a):
    return "You're a(n) "+{(a<13):'kid',(a>12):'teenager',(a>17):'adult',(a>64):'elderly'}[True]

# task is made it short. use ternary operators or tricks
# classic ternary
f"You're a(n) {a<13 and 'kid' or a<18 and 'teenager' or a<65 and 'adult' or 'elderly'}"
# trick with indexing
f"You're a(n) {['kid','teenager','adult','elderly'][(age > 12)+(age > 17)+(age >64)]}"
# trick with consiquence ordering
f"You're a(n) {'kid'*(a<13) or 'teenager'*(12<a<18) or 'adult'*(17<a<65) or 'elderly'}"
