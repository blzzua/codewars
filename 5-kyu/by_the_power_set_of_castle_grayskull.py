# https://www.codewars.com/kata/53d3173cf4eb7605c10001a8

import itertools
# https://more-itertools.readthedocs.io/en/stable/_modules/more_itertools/recipes.html#powerset
def power(a):
    return itertools.chain.from_iterable(itertools.combinations(a, r) for r in range(len(a) + 1))


#native superset wo itertols
  res = [[]]
  for x in s: res.extend([q + [x] for q in res])
  return res

# wtf? 
def power(x):
    def f(s):
        x = len(s)
        masks = [1 << i for i in range(x)]
        for i in range(1 << x):
            yield [ss for mask, ss in zip(masks, s) if i & mask]
    return sorted(list(f(x)))
