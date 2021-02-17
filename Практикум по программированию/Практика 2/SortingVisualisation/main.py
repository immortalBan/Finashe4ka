from tkinter import *
import random
import ValueClass


def setup():
    global root, canvas, width, height, values, i, last_index, step
    
    width = height = 720
    
    root = Tk()
    canvas = Canvas(root, width=width, height=height, bg="#fff2fa")
    canvas.pack()
    
    values = []
    
    for j in range(width):
        values.append(ValueClass.Value((0, height)))
    
    i = 0
    last_index = len(values) - 1
    step = len(values)//2
    
    for j in range(len(values)):
        canvas.create_line(j+1, (height + values[j].value) / 2, j+1, (height - values[j].value) / 2, fill = values[j].color)

def bubble_sort():
    
    global i
    
    if i < len(values):
        for j in range(len(values) - i - 1):
            if values[j].value > values[j + 1].value:
                values[j], values[j + 1] = values[j + 1], values[j]
    else:
        return
    
    canvas.delete("all")
    
    for j in range(len(values)):
        canvas.create_line(j+1, (height + values[j].value) / 2, j+1, (height - values[j].value) / 2, fill = values[j].color)
        
    i += 1
    
    root.after(1, bubble_sort)
    


def main():
    
    setup()

    bubble_sort()
    
    root.mainloop()

main()
