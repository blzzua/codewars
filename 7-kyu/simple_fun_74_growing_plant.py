# https://www.codewars.com/kata/58941fec8afa3618c9000184

def growing_plant(up_speed, down_speed, desired_height):
    day = 0
    current_heigth = 0
    while current_heigth < desired_height: 
        day += 1
        current_heigth += up_speed
        if current_heigth < desired_height:
            current_heigth -= down_speed
        else:
            return day
    return 1

