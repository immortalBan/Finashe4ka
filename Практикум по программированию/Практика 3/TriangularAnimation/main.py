from tkinter import * 
import math


spacing = 5
theta = 0
angle_step = 30
moving = True

def polarToCartesian(radius, angle):
    angle += angle_step
    return list((radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle))))

def lerp (array1, array2, interpolation):
    new_x = array1[0] + interpolation * (array2[0] - array1[0])
    new_y = array1[1] + interpolation * (array2[1] - array1[1])
    return list((new_x, new_y))

width = height = 720 
radius = 300
center = [width // 2, height // 2]

def get_path():
    cirPath = []
    triPath = []

    startA = 0
    endA = 120

    start = polarToCartesian(radius, startA)
    end = polarToCartesian(radius, endA)
    
    for i in range(startA, 360, spacing):
        cv = polarToCartesian(radius, i)
        cirPath.append(cv.copy())
        amt = i % 120 / (endA - startA)
        tv = lerp(start, end, amt)
        triPath.append(tv.copy())
        
        if (i + spacing) % 120 == 0:
            startA = startA + 120
            endA = endA + 120;
            start = polarToCartesian(radius, startA)
            end = polarToCartesian(radius, endA)
    return cirPath, triPath
        
root = Tk()
canvas = Canvas(root, width=width, height=height, bg="white")
canvas.pack()

    
def draw():
    global theta, angle_step
    
    canvas.delete("all")
    
    amt = (math.sin(math.radians(theta)) + 1) / 2
    theta += 5
    cirPath, triPath = get_path()
    cv = cirPath[0].copy()
    tv = triPath[0].copy()
    x, y = lerp(cv, tv, amt)
    for i in range(len(cirPath)):
        cv = cirPath[i].copy()
        tv = triPath[i].copy()
        x_old, y_old = x, y
        x, y = lerp(cv, tv, amt)
        canvas.create_line(x_old + width // 2, y_old + height // 2, x + width // 2, y + height // 2)
    cv = cirPath[0].copy()
    tv = triPath[0].copy()
    x_old, y_old = x, y
    x, y = lerp(cv, tv, amt)
    canvas.create_line(x_old + width // 2, y_old + height // 2, x + width // 2, y + height // 2)
    
    if moving:
        angle_step += 1
    
    root.after(20, draw)
    
draw()
root.mainloop()
        