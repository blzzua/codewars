# https://www.codewars.com/kata/62ad72443809a4006998218a

FSM = {
        (Nothing,Like) : Like,
        (Nothing,Dislike) : Dislike,
        (Like,Like) : Nothing,
        (Like,Dislike) : Dislike,
        (Dislike,Like) : Like,
        (Dislike,Dislike) : Nothing
    }
def like_or_dislike(lst):
    state = Nothing
    for tap in lst:
        state = FSM.get( (state, tap) )
    return state


