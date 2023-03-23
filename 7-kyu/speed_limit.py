# https://www.codewars.com/kata/635a7827bafe03708e3e1db6

def fine(diff):
    if diff < 10:
        fine = 0
    elif 10 <= diff <= 19:
        fine = 100
    elif 20 <= diff <= 29:
        fine = 250
    elif 30 <= diff:
        fine = 500
    return fine

def speed_limit(speed, signals):
    return sum(fine(speed - signal) for signal in signals)
