from tkinter import *
import math

width = height = 600

center_x = width // 2
center_y = height // 2

R_x = 200
R_y = 150
r = 20
way = 1
angle = 0
angle_0 = 0
frequency = 20
step = way * frequency / 100
step_0 = way * frequency  / 2
speed = 1 
amplitude = 3

def renormalize(n, range1, range2):
    
    delta1 = range1[1] - range1[0]
    delta2 = range2[1] - range2[0]
    
    return (delta2 * (n - range1[0]) / delta1) + range2[0]

def get_new_coords (R_x, R_y, r, center_x, center_y, angle, way): 
    x1 = center_x -(math.sin(math.radians(angle)) * R_x * (math.sin(math.radians(angle_0)) + amplitude)/(amplitude)) - r
    y1 = center_y -(way * math.cos(math.radians(angle)) * R_y * (math.sin(math.radians(angle_0)) + amplitude)/(amplitude)) - r
    x2 = center_x -(math.sin(math.radians(angle)) * R_x * (math.sin(math.radians(angle_0)) + amplitude)/(amplitude)) + r
    y2 = center_y -(way * math.cos(math.radians(angle)) * R_y * (math.sin(math.radians(angle_0)) + amplitude)/(amplitude)) + r
    return x1, y1, x2, y2
    
 
def motion():
    global angle, angle_0, way, speed
    if angle >= 360:
        angle = 0
    if angle_0 >= 360:
        angle_0 = 0
    way_prev = way
    way = scale_way.get() * 2 - 3
    if way != way_prev:
        angle = 180 - angle
        angle_0 = 180 - angle_0
    speed = int(renormalize(scale_speed.get(), (0, 10), (10, 1)))
    x1, y1, x2, y2 = get_new_coords(R_x, R_y, r, center_x, center_y, angle, way)
    x1_old, y1_old, x2_old, y2_old = c.coords(point_figure)
    c.coords(point_figure, x1, y1, x2, y2)
    c.create_line(abs(x1_old+x2_old)/2-1, abs(y1_old+y2_old)/2-1, abs(x1+x2)/2, abs(y1+y2)/2, fill = "#C71585", width = 1)
    angle += step
    angle_0 += step_0
    root.after(speed, motion)
 
    
    
if __name__ == "__main__":
    root = Tk()
    c = Canvas(root, width=width, height=height, bg="#fff2fa")
    scale_speed = Scale(root, from_=1, to=10, orient=HORIZONTAL)
    scale_way = Scale(root, from_=1, to=2, orient=HORIZONTAL)
    label1 = Label(root, width=30, height=2)
    label2 = Label(root, width=20, height=2)
    c.pack()
    label1.pack(side=LEFT)
    scale_speed.pack(side=RIGHT)
    scale_way.pack(side=LEFT)
    label2.pack(side=RIGHT)
    label1['text'] = "Направление движения \n(1 - по часовой, 2 - против часовой)"
    label2['text'] = "Скорость движения"
    
    main_figure = c.create_oval(center_x - R_x, center_y - R_y, center_x + R_x, center_y + R_y, fill='#008B8B', outline = "#008B8B")
    point_figure = c.create_oval(center_x - r, center_y - r - R_y, center_x + r, center_y + r - R_y, fill='#FF1493', outline = "#FF1493")
    
    motion() 
    root.mainloop()

