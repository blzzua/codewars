# https://www.codewars.com/kata/539de388a540db7fec000642

from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    cd = datetime.strptime(current_date, '%B %d, %Y')
    ed = datetime.strptime(expiration_date, '%B %d, %Y')
    if entered_code is correct_code and  cd <= ed:
        return True
    else:
        return False
    

