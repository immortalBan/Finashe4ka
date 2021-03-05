from tkinter import *
import CellClass


width = height = 720
w = 40

cols = width // w
rows = height // w

cells_grid = []
cells_stek = []

root = Tk()
canvas = Canvas(root, width=width, height=height, bg="black")
canvas.pack()

for i in range(cols):
    for j in range(rows):
        cells_grid.append(CellClass.Cell(i, j, canvas, w))

current = cells_grid[0]
def removeWalls(cell1, cell2):
    x = cell1.i - cell2.i
    if x == 1:
        cell1.walls[3] = False
        cell2.walls[1] = False
    elif x == -1:
        cell2.walls[3] = False
        cell1.walls[1] = False
    
    y = cell1.j - cell2.j
    if y == 1:
        cell1.walls[0] = False
        cell2.walls[2] = False
    elif y == -1:
        cell2.walls[0] = False
        cell1.walls[2] = False
        

def draw():
    
    global current
    
    canvas.delete("all")
    
    for cell in cells_grid:
        cell.show()
    
    current.visited = True
    current.highlight()
    
    next_cell = current.checkNeighbours(cells_grid)
    if next_cell:
        next_cell.visited = True
        
        cells_stek.append(current)
        
        removeWalls(current, next_cell)
        
        current = next_cell
    elif len(cells_stek) > 0:
        current = cells_stek.pop()
    
    
    root.after(10, draw)
        
draw()
root.mainloop()       