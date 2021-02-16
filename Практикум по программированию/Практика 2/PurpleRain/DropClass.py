import random
from constants import *
from tkinter import *

def renormalize(n, range1, range2):
    
    delta1 = range1[1] - range1[0]
    delta2 = range2[1] - range2[0]
    
    return (delta2 * (n - range1[0]) / delta1) + range2[0]

class Drop:
    
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(-height//2, 0)
        self.z = random.randint(0, 20)
        self.length = renormalize(self.z, (0, 20), (10, 20))
        self.speed  = renormalize(self.z, (0, 20), (1, 20))
        self.grav = renormalize(self.z, (0, 20), (0.05, 0.2))
        self.thick = renormalize(self.z, (0, 20), (1, 3))
    
    def fall(self):
        self.y += self.speed
        self.speed += self.grav
        if self.y > height:
            self.y = self.y = random.randint(-height//2, 0)
            self.speed  = renormalize(self.z, (0, 20), (1, 20))
            
    def show(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.thick, self.y + self.length, fill="#8b00ff", outline = "#8b00ff")
