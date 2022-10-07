# https://www.codewars.com/kata/57d4e99bec16701a67000033

def heavy_metal_umlauts(boring_text):
    return boring_text.translate(boring_text.maketrans('AEIOUYaeiouy','ÄËÏÖÜŸäëïöüÿ'))


