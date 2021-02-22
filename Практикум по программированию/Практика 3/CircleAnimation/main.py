from tkinter import *
import math

width = 750 
height = 750

R = 300

circle_coords = [width//2 - R, height // 2 - R, width//2 + R, height // 2 + R]

main_angles = [90 + 120 * index for index in range(3)]

main_points = [(R * math.sin(math.radians(180 + 120 * index)) + width // 2, R * math.cos(math.radians(180 + 120 * index)) + height // 2) for index in range(3)]

bool_lines = [False, False, False]

current_angle = 330

step = 1

root = Tk()
canvas = Canvas(root, width=width, height=height, bg="white")
canvas.pack()

def get_coords(angle, radius):
    return (radius * math.sin(math.radians(angle+90)) + width // 2, radius * math.cos(math.radians(angle+90)) + height // 2)


def start():
    root.after(500, draw)


def draw():
    global current_angle
    canvas.delete("all")
    current_angle = current_angle % 360
    
    if step > 0:
        if current_angle == main_angles[0]:
            bool_lines[2] = True
        elif current_angle == main_angles[1] and bool_lines[2]:
            bool_lines[0] = True
        elif current_angle == main_angles[2] and bool_lines[0]:
            bool_lines[1] = True
    else:
        if current_angle == main_angles[1]:
            bool_lines[1] = True
        elif current_angle == main_angles[0] and bool_lines[1]:
            bool_lines[0] = True
        elif current_angle == main_angles[2] and bool_lines[0]:
            bool_lines[2] = True
    
    
    if bool_lines[0]:
        canvas.create_line(*main_points[0], *main_points[1], fill='gray25', width=2)
    elif not main_angles[0] <= current_angle <= main_angles[1]:
        canvas.create_arc(*circle_coords, start = main_angles[0], extent = 120, style=ARC, outline='gray25', width=2)
    elif step > 0:
        canvas.create_line(*main_points[0], *get_coords(current_angle, R), fill='gray25', width=2)
        canvas.create_arc(*circle_coords, start = current_angle, extent = main_angles[1] - current_angle, style=ARC, outline='gray25', width=2)
    else:
        canvas.create_line(*get_coords(current_angle, R), *main_points[1],  fill='gray25', width=2)
        canvas.create_arc(*circle_coords, start = main_angles[0], extent = current_angle - main_angles[0], style=ARC, outline='gray25', width=2)
    if bool_lines[1]:
        canvas.create_line(*main_points[1], *main_points[2], fill='gray25', width=2)
    elif not main_angles[1] <= current_angle <= main_angles[2]:
        canvas.create_arc(*circle_coords, start = main_angles[1], extent = 120, style=ARC, outline='gray25', width=2)
    elif step > 0:
        canvas.create_line(*main_points[1], *get_coords(current_angle, R), fill='gray25', width=2)
        canvas.create_arc(*circle_coords, start = current_angle, extent = main_angles[2] - current_angle, style=ARC, outline='gray25', width=2)
    else:
        canvas.create_line(*get_coords(current_angle, R), *main_points[2], fill='gray25', width=2)
        canvas.create_arc(*circle_coords, start = main_angles[1], extent = current_angle - main_angles[1], style=ARC, outline='gray25', width=2) 
    if bool_lines[2]:
        canvas.create_line(*main_points[2], *main_points[0], fill='gray25', width=2)
    elif not main_angles[2] <= current_angle <= 360 and not current_angle <= main_angles[0]:
        canvas.create_arc(*circle_coords, start = main_angles[2], extent = 119.8, style=ARC, outline='gray25', width=2)
    elif step > 0:
        canvas.create_line(*main_points[2], *get_coords(current_angle, R), fill='gray25', width=2)
        if current_angle <= 360:
            canvas.create_arc(*circle_coords, start = current_angle, extent = main_angles[0] + 360 - current_angle - 0.2, style=ARC, outline='gray25', width=2)
        else:
            canvas.create_arc(*circle_coords, start = current_angle, extent = main_angles[0] - current_angle - 0.2, style=ARC, outline='gray25', width=2)
    else:
        canvas.create_line(*get_coords(current_angle, R), *main_points[0], fill='gray25', width=2)
        if current_angle <= 360:
            canvas.create_arc(*circle_coords, start = main_angles[2], extent = current_angle + 360 - main_angles[2] - 0.2, style=ARC, outline='gray25', width=2)
        else:
            canvas.create_arc(*circle_coords, start = current_angle, extent = current_angle - main_angles[2] - 0.2, style=ARC, outline='gray25', width=2)
    current_angle += step
    root.after(10, draw)


start()
root.mainloop()