# https://www.codewars.com/kata/57ed40e3bd793e9c92000fcb

def correctness(bobs_decisions, expert_decisions): 
    return sum(1 if a == b else 0.5 if  a == '?' or b == '?' else 0 for a,b in zip(bobs_decisions, expert_decisions))


