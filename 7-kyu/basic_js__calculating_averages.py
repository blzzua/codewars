# https://www.codewars.com/kata/529f32794a6db5d32a00071f

class Calculator:
    @staticmethod
    def average(*args):
        try:
            return sum(args)/len(args)
        except:
            return 0

