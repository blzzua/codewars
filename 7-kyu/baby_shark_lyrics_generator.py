# https://www.codewars.com/kata/5d076515e102162ac0dc514e

def baby_shark_lyrics():
    s=' shark';S=['Baby'+s,'Mommy'+s,'Daddy'+s,'Grandma'+s,'Grandpa'+s,"Let's go hunt"] 
    return '\n'.join((s+','+' doo'*6+'\n')*3+s+'!' for s in S)+'\nRun away,…'
    

