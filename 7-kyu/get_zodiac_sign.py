# https://www.codewars.com/kata/5a376259b6cfd77ca000006b

def get_zodiac_sign(day, month):
    m_index = month - 1
    HORIZON = [19, 18, 20, 19, 20, 20, 22, 22, 22, 22, 21, 21, 19]
    if day <= HORIZON[m_index]:
        return SIGNS[m_index]
    else:
        return SIGNS[(m_index + 1 ) % 12]
