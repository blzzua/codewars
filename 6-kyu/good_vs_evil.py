# https://www.codewars.com/kata/52761ee4cffbc69732000738

def good_vs_evil(good, evil):
    good_score = sum(cnt * score for cnt, score in zip(map(int,good.split(' ')), [1,2,3,3,4,10] ))
    evil_score = sum(cnt * score for cnt, score in zip(map(int,evil.split(' ')), [1,2,2,2,3,5,10] ))
    return 'Battle Result: '+ {\
       good_score == evil_score: 'No victor on this battle field',
       good_score > evil_score: 'Good triumphs over Evil',
       good_score < evil_score: 'Evil eradicates all trace of Good'}[True]
