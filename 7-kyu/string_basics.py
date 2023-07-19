# https://www.codewars.com/kata/56326c13e63f90538d00004e

def get_users_ids(string):
    return [word.replace('uid', '', 1).strip() for word in string.lower().replace('#', '').split(',')]
  
