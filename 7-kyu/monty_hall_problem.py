# https://www.codewars.com/kata/54f9cba3c417224c63000872

def monty_hall(correct_door_number, participant_guesses):
    return round(len([x for x in participant_guesses if x != correct_door_number]) / len(participant_guesses)*100)

