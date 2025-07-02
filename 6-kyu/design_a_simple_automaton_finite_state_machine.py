# https://www.codewars.com/kata/5268acac0d3f019add000203

class Automaton(object):
    def __init__(self):
        self.state = 'q1'

    def read_commands(self, commands):
        for cmd in commands:
            match self.state:
                case 'q1':
                    self._do_cmd_state_q1(cmd)
                case 'q2':
                    self._do_cmd_state_q2(cmd)
                case 'q3':
                    self._do_cmd_state_q3(cmd)

        if self.state == 'q2':
            return True
        else:
            return False
    
    def _do_cmd_state_q1(self, cmd):
        if cmd == "1":
            self.state = 'q2'

    def _do_cmd_state_q2(self, cmd):
        if cmd == "0":
            self.state = 'q3'
    
    def _do_cmd_state_q3(self, cmd):
        if cmd in ("0","1"):
            self.state = 'q2'
            
my_automaton = Automaton()
