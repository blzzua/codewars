# https://www.codewars.com/kata/587ac5616d360f6bed000088

class Grid():
    def __init__(self, width, height):
        self.chart = ['0' * width ] * height

    def plot_point(self, x, y):
        self.chart[y-1] = ''.join('X' if i == x else '0' for i in range(1,len(self.chart[y])+1))
    
    @property
    def grid(self):
        return '\n'.join(self.chart)

    def __repr__(self):
        return self.grid
