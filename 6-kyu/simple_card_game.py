# https://www.codewars.com/kata/53417de006654f4171000587

cards = {score:val  for val, score in enumerate(['2','3','4','5','6','7','8','9','T','J','Q','K','A'])}
def winner(deck_steve, deck_josh):
    j_score, s_score = 0,0
    for j, s in zip(deck_josh, deck_steve):
        if j == s:
            continue
        elif cards.get(j) > cards.get(s):
            j_score += 1
        else:
            s_score += 1
    return {j_score > s_score: f'Josh wins {j_score} to {s_score}',
            j_score < s_score: f'Steve wins {s_score} to {j_score}',
            j_score == s_score: f'Tie'}[True]
    
