# https://www.codewars.com/kata/559f860f8c0d6c7784000119

def any_arrows(arrows):
    return any(not a.get('damaged', False) for a in arrows)

