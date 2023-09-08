# https://www.codewars.com/kata/5872637c2eefcb1216000081

def destroyer(input_sets):
    sets = set.union(*input_sets)
    tr = str.maketrans({k: '_' for k in sets})
    return 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.translate(tr)
