# https://www.codewars.com/kata/5470ae03304c1250b4000e57

def identify_weapon(character):
    return {
            'Laval': 'Laval-Shado Valious',
            'Cragger': 'Cragger-Vengdualize',
            'Lagravis': 'Lagravis-Blazeprowlor',
            'Crominus': 'Crominus-Grandorius',
            'Tormak': 'Tormak-Tygafyre',
            'LiElla': 'LiElla-Roarburn',
           }.get(character, 'Not a character')
  
