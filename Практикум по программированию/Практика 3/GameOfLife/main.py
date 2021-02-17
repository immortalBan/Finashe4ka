from tkinter import *
import random
import CellClass


width = height = 600
w = 10

cols = width // w
rows = height // w

cells_grid = []

root = Tk()
canvas = Canvas(root, width=width, height=height, bg="black")
canvas.pack()

for i in range(cols):
    temp_list = []
    for j in range(rows):
        alive = bool(random.randint(0, 2))
        cells_grid.append(CellClass.Cell(i, j, canvas, w, alive))
   # cells_grid.append(temp_list)

for cell in cells_grid:
    cell.checkNeighbours(cells_grid)

def draw():
    
    canvas.delete("all")
    
    for cell in cells_grid:
        cell.update_phase_one()
    
    for cell in cells_grid:
        cell.update_phase_two()
        cell.show()
       
    root.after(50, draw)
        
draw()
root.mainloop() 