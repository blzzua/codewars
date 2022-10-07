# https://www.codewars.com/kata/56ff1667cc08cacf4b00171b

def count_vegetables(string):
    vegetables = ["cabbage", "carrot", "celery", "cucumber", "mushroom", 
                  "onion", "pepper", "potato", "tofu", "turnip" ]
    return sorted([(string.split(' ').count(v), v) for v in vegetables], key=lambda i: (i[0], i[1]), reverse=True)



