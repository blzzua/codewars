# https://www.codewars.com/kata/5a6d3bd238f80014a2000187

def owned_cat_and_dog(cat_years, dog_years):
    if cat_years < 15:
        hyc = 0
    elif cat_years - 15 < 9:
        hyc = 1
    else:
        hyc = (cat_years - 15 - 9 ) // 4 + 2

    if dog_years < 15:
        hyd = 0
    elif dog_years - 15 < 9:
        hyd = 1
    else:
        hyd = (dog_years - 15 - 9 ) // 5 + 2

    return [hyc, hyd]

# clever math
#   hyc = (cat_years > 14 ) + (cat_years > 23) + max(0, (cat_years - 24) // 4)
#   hyd = (dog_years > 14 ) + (dog_years > 23) + max(0, (dog_years - 24) // 5)
