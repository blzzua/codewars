# https://www.codewars.com/kata/590fca79b5f8a69285000465

def apples_distribution(apples, capacity, max_left):
    return sum(1 for i in range(1, min(apples, capacity) + 1) if apples % i <= max_left)


