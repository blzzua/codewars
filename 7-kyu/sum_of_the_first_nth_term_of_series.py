# https://www.codewars.com/kata/555eded1ad94b00403000071

def series_sum(n):
    return "{:.2f}".format(round(sum(1.0/(3*i-2) for i in range(1, n+1)),2))

