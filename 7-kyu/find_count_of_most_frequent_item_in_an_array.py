# https://www.codewars.com/kata/56582133c932d8239900002e
  
def most_frequent_item_count(c):
    return max([c.count(i) for i in c], default=0)
