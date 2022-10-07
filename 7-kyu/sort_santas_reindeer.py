# https://www.codewars.com/kata/52ab60b122e82a6375000bad

def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=lambda x:(x.split())[1])

