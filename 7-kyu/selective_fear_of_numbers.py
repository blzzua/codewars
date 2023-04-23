# https://www.codewars.com/kata/55b1fd84a24ad00b32000075

def am_I_afraid(day,num):
    return any((
        (day == 'Monday' and num == 12),
        (day == 'Tuesday' and num > 95),
        (day == 'Wednesday' and num == 34),
        (day == 'Thursday' and num == 0),
        (day == 'Friday' and num % 2 == 0),
        (day == 'Saturday' and num == 56),
        (day == 'Sunday' and abs(num) == 666)
        ))
