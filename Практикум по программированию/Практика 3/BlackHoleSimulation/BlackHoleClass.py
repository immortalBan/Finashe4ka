from constants import *

class BlackHole:
    
    def __init__(self, x, y, m, canvas):
        self.pos = list((x, y))
        self.mass = m
        self.rs = (2 * G * self.mass) / (c * c * 3)
        self.canvas = canvas
    
    def show(self):
        self.canvas.create_oval(self.pos[0] - self.rs, self.pos[1] - self.rs, self.pos[0] + self.rs, self.pos[1] + self.rs, fill = "black")
        
        self.canvas.create_oval(self.pos[0] - self.rs * 3, self.pos[1] - self.rs * 3 , self.pos[0] + self.rs * 3 , self.pos[1] + self.rs * 3 , outline = "#A9A9A9", width = 32)
                                
        self.canvas.create_oval(self.pos[0] - self.rs * 1.5, self.pos[1] - self.rs * 1.5, self.pos[0] + self.rs * 1.5 , self.pos[1] + self.rs * 1.5 , outline = "#FF8C00", width = 16)
                                
    def pull(self, photon):
        force = subVector(self.pos, photon.pos)
        r = lengthVector(force)
        fg = G * self.mass / (r * r)
        forse = normalizeVector(force)
        force = multVector(force, fg)
        photon.vel = addVector(photon.vel, force)
        photon.vel = normalizeVector(photon.vel)
        photon.vel = multVector(photon.vel, c)
        if (r < self.rs):
            photon.stop()
    
    def show_main_hole(self):
        self.canvas.create_oval(self.pos[0] - self.rs, self.pos[1] - self.rs, self.pos[0] + self.rs, self.pos[1] + self.rs, fill = "black")
