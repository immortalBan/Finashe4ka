class Cell:
    
    def __init__(self, i, j, canvas, width, alive):
        self.i = i
        self.j = j
#        self.walls = [True, True, True, True]
        self.alive = alive
        self.new_alive = None
        self.neighbours = []
        self.width = width
        self.canvas = canvas
    
    def checkNeighbours (self, cells_list):
        
        top = right = left = bottom = top_right = top_left = bottom_right = bottom_left = None
        
        for cell in cells_list:
            if cell.i == self.i and cell.j == self.j-1:
                top = cell
            if cell.i == self.i + 1 and cell.j == self.j:
                right = cell
            if cell.i == self.i and cell.j == self.j+1:
                bottom = cell
            if cell.i == self.i - 1 and cell.j == self.j:
                left = cell
            if cell.i == self.i + 1 and cell.j == self.j-1:
                top_right = cell
            if cell.i == self.i - 1 and cell.j == self.j - 1:
                top_left = cell
            if cell.i == self.i + 1 and cell.j == self.j+1:
                bottom_right = cell
            if cell.i == self.i - 1 and cell.j == self.j + 1:
                bottom_left = cell
        
        
        if top:
            self.neighbours.append(top)
        if right:
            self.neighbours.append(right)
        if bottom:
            self.neighbours.append(bottom)
        if left:
            self.neighbours.append(left)
        if top_right:
            self.neighbours.append(top_right)
        if top_left:
            self.neighbours.append(top_left)
        if bottom_right:
            self.neighbours.append(bottom_right)
        if bottom_left:
            self.neighbours.append(bottom_left)
    
    def update_phase_one(self):
        amount = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                amount += 1
        
        if not self.alive and amount == 3:
            self.new_alive = True
        elif self.alive and amount not in [2, 3]:
            self.new_alive = False
        else:
            self.new_alive = self.alive
    def update_phase_two(self):
        self.alive = self.new_alive
        self.new_alive = None
    
    def show(self):
        x = self.i * self.width
        y = self.j * self.width
        if self.alive:
            self.canvas.create_rectangle(x, y, x + self.width, y + self.width, fill = '#ffffff', outline = "#ffffff")
        