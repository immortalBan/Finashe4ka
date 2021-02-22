from constants import *

class MovingObjectClass:
    
    def __init__ (self, x, y, mass, canvas):
        self.pos = [x, y]
        self.vel = [0, 0]
        self.acc = [0, 0]
        self.mass = mass
        self.radius = self.mass ** 0.5 * 10
        self.canvas = canvas
        
    def edges (self):
        if self.pos[1] >= height - self.radius:
            self.pos[1] = height - self.radius
            self.vel[1] *= -0.9
    
        if self.pos[0] >= width - self.radius:
            self.pos[0] = width - self.radius
            self.vel[0] *= -0.9
        elif self.pos[0] <= self.radius:
            self.pos[0] = self.radius
            self.vel[0] *= -0.9
        
    def drag (self, dragC):
        
        drag = self.vel.copy()
        drag = normalizeVector(drag)
        drag = multVector(drag, -1)
        speedSq = lengthVector(self.vel) ** 2
        drag = multVector(drag, dragC * speedSq * self.mass * 0.0095 * self.radius)
        self.applyForce(drag)
        
    def applyForce(self, force):
        f = multVector(force, 1 / self.mass)
        self.acc = addVector(self.acc, f)
    
    def update (self):
        self.vel = addVector(self.vel, self.acc)
        self.pos = addVector(self.pos, self.vel)
        self.acc = [0, 0]
    
    def show (self):
        self.canvas.create_oval(self.pos[0] - self.radius, self.pos[1] - self.radius, self.pos[0] + self.radius, self.pos[1] + self.radius, outline = 'white', fill = 'gray12')