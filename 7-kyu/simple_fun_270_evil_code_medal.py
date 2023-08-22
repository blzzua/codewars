# https://www.codewars.com/kata/5915686ed2563aa6650000ab

def evil_code_medal(user_time, gold, silver, bronze):
    return {
            user_time < bronze: 'Bronze',
            user_time < silver: 'Silver',
            user_time < gold: 'Gold',
           }.get(True, 'None')
