# https://www.codewars.com/kata/580751a40b5a777a200000a1

def vowel_one(s):
    return ''.join(map(str,map(int,map(lambda x: x in 'aeiouAEIOU', s))))
  
