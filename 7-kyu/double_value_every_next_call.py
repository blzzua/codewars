# https://www.codewars.com/kata/632408defa1507004aa4f2b5
class Class:
    power = -1
    
    @staticmethod
    def get_number():
        Class.power += 1
        return 2 ** Class.power
