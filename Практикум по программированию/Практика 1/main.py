from tkinter import *
import math

width = 600
height = 600
centerx = width / 2
centery = height / 2
R = 200
r = 20
ygol = 0
skor = 0.1
napr = 1 
 

def get_new_coords (R, r, centerx, centery, ygol, napr):
    x = centerx - (math.sin(math.radians(ygol)) * R)
    y = centery - (napr * math.cos(math.radians(ygol)) * R)
    return x, y
    
 
def motion():
    global ygol, napr, skor
    if ygol >= 360:
        ygol = 0
    x, y = get_new_coords(R, r, centerx, centery, ygol, napr)
    c.coords(small_circle, x-r, y-r, x+r, y+r)
    ygol += skor
    root.after(10, motion)
 
    
    
if __name__ == "__main__":
    root = Tk()
    c = Canvas(root, width=width, height=height, bg="white")
    c.pack()
    
    main_circle = c.create_oval(centerx - R, centery - R, centerx + R, centery + R, fill='green')
    small_circle = c.create_oval(centerx - r - R, centery - r, centerx + r - R, centery + r, fill='red')
    
    motion() 
    root.mainloop()

