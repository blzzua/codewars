# https://www.codewars.com/kata/55e8beb4e8fc5b7697000036

def move(self, direction):
    x = int(self.position[0])
    y = int(self.position[1])
    if direction == 'up':
        x -= 1
    elif direction == 'down':
        x += 1
    elif direction == 'left':
        y -= 1
    elif direction == 'right':
        y += 1
    if  any((x < 0, x > 4, y < 0, y > 4)):
        raise Error
    self.position = str(x)+str(y)
        
Hero.move = move
