# https://www.codewars.com/kata/54b81566cd7f51408300022d

def word_search(query, seq):
    return [w for w in seq if query.lower() in w.lower()] or ['None']
