# https://www.codewars.com/kata/56069d0c4af7f633910000d3

def search(budget,prices):
    return ','.join(map(str,sorted(filter(lambda price:price<=budget,prices))))

