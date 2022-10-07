# https://www.codewars.com/kata/55b75fcf67e558d3750000a3

class Block:
    def __init__(self, dim):
        self.width, self.length, self.height = dim
        
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height
    
    def get_surface_area(self):
        return 2 * (self.width * self.length + self.length * self.height + self.width * self.height)
    

