# https://www.codewars.com/kata/53f0f358b9cb376eca001079

class Ball(object):
    def __init__(self,arg = None):
        if arg is None:
            self.ball_type  = 'regular'
        else:
            self.ball_type  = arg


