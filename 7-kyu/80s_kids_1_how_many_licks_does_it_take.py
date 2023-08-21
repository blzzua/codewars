# https://www.codewars.com/kata/566091b73e119a073100003a

def total_licks(env):
    ls = 252
    if env:
        ls += sum(env.values())
        mx = max(env.values())
        ch = max(env, key=env.get)
        if ch and mx > 0:
            return f'It took {ls} licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was {ch}.'
    return f'It took {ls} licks to get to the tootsie roll center of a tootsie pop.'
