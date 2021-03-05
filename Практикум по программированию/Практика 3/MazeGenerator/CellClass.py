import random

class Cell:
    
    def __init__(self, i, j, canvas, width):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False
        self.canvas = canvas
        self.width = width
        
    
    def checkNeighbours (self, cells_list):
        neighbours = []
        
        top = right = left = bottom = None
        
        for cell in cells_list:
            if cell.i == self.i and cell.j == self.j-1:
                top = cell
            if cell.i == self.i + 1 and cell.j == self.j:
                right = cell
            if cell.i == self.i and cell.j == self.j+1:
                bottom = cell
            if cell.i == self.i - 1 and cell.j == self.j:
                left = cell
        
        
        if (top != None and not top.visited):
            neighbours.append(top)
        if (right != None and not right.visited):
            neighbours.append(right)
        if (bottom != None and not bottom.visited):
            neighbours.append(bottom)
        if (left != None and not left.visited):
            neighbours.append(left)
        
        if len(neighbours) > 0:
            index = random.randint(0, len(neighbours)-1)
            return neighbours[index]
        else:
            return None
    
    def highlight(self):
        x = self.i * self.width
        y = self.j * self.width
        self.canvas.create_rectangle(x, y, x + self.width, y + self.width, fill = '#ce5a57', outline = "#ce5a57")
                                    
    def show(self):
        x = self.i * self.width
        y = self.j * self.width
        if self.visited:
           self.canvas.create_rectangle(x, y, x + self.width, y + self.width, fill = '#e1b16a', outline = "#e1b16a")
        
        if (self.walls[0]):
            self.canvas.create_line(x    , y    , x + self.width, y, fill="white")
        if (self.walls[1]):
            self.canvas.create_line(x + self.width, y    , x + self.width, y + self.width, fill="white")
        if (self.walls[2]):
            self.canvas.create_line(x + self.width, y + self.width, x    , y + self.width, fill="white")
        if (self.walls[3]):
            self.canvas.create_line(x    , y + self.width, x    , y, fill="white")
        
        
        
                