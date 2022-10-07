# https://www.codewars.com/kata/57613fb1033d766171000d60

def uefa_euro_2016(teams, scores):
    if scores[0] == scores[1]:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."
    else:
        return f"At match {teams[0]} - {teams[1]}, {teams[int(scores[0] < scores[1])]} won!"

