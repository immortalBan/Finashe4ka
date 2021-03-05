from constants import *

class Photon:
    
    def __init__(self, x, y, canvas):
        self.pos = list((x, y))
        self.vel = list((-c, 0))
        self.history = []
        self.stopped = False
        self.theta = 0
        self.canvas = canvas
    
    def stop(self):
        self.stopped = True
        
    def update(self):
        if not self.stopped:
            self.history.append(self.pos.copy())
            deltaV = self.vel.copy()
            deltaV = multVector(deltaV, dt)
            self.pos = addVector(self.pos, deltaV)
        if len(self.history) > 500:
            self.history.pop(0)
    
    def show(self):
        self.canvas.create_oval(self.pos[0] - 1, self.pos[1] - 1, self.pos[0] + 1, self.pos[1] + 1, fill = "red", outline = "red")
        
        x = self.history[0][0]
        y = self.history[0][1]
        
        for v in self.history:
            x_old = x
            y_old = y
            x = v[0]
            y = v[1]
            self.canvas.create_line(x_old, y_old, x, y, fill = "red")
        self.canvas.create_line(self.pos[0], self.pos[1], x, y, fill = "red")
        