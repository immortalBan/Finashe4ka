class Checker:

    def __init__(self, color, pos_x, pos_y):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y

    def check_queen(self):
        if self.color == 'white' and self.pos_y == 7:
            return True
        elif self.color == 'black' and self.pos_y == 0:
            return True
        else:
            return False
