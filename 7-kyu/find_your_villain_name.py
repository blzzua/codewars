# https://www.codewars.com/kata/536c00e21da4dc0a0700128b

def get_villain_name(birthdate):
    first = ["Zero", "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    m,y = birthdate.month, birthdate.day
    return f'{first[m]} {last[y%10]}'

