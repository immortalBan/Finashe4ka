from tkinter import *
from constants import *
import random
import MovingObjectClass

def setup ():
    global moving_objects, dragC, canvas, root, gravity, wind
    
    gravity = [0, 0.1]
    wind = [0, 0]
    dragC = 0.1
    
    root = Tk()
    canvas = Canvas(root, width=width, height=height, bg="black")
    canvas.pack()
    
    moving_objects = []
    
    for i in range(5):
        moving_objects.append(MovingObjectClass.MovingObjectClass(random.randint(0, width), 0, random.randint(10, 40), canvas))
    

def draw ():
    global canvas, root, moving_objects, wind
    
    canvas.delete("all")
    
    for moving_object in moving_objects:
        weight = multVector(gravity, moving_object.mass)
        moving_object.applyForce(weight)
        if moving_object.pos[1] > height  * 2 / 5 and moving_object.pos[1] < height * 5 / 5:
            moving_object.drag(dragC)
        moving_object.applyForce(wind)
        moving_object.update()
        moving_object.edges()
        moving_object.show()
    
    canvas.create_rectangle(0, height * 2 / 5, width, height * 5 / 5, fill = 'gray25', stipple = 'gray25', outline = 'gray12')
    
    root.after(10, draw)
    
setup()
draw()
root.mainloop()