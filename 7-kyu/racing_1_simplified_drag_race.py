# https://www.codewars.com/kata/5a40f5b01f7f70ed7600001e

def drag_race(length, anna, bob):
    for car in (anna,  bob):
        car.time = car.reaction_time + length / car.speed
    if anna.time == bob.time:
        return "It's a draw"
    if anna.time > bob.time:
        return "Bob is the winner"
    else:
        return "Anna is the winner"
