class Field:

    board_dict = {"black": "⬛️", "white": "⬜️"}
    figure_dict = {"black": "🌚", "white": "🌝", "queen": "😏"}

    def __init__(self, coords_x, coords_y, checker=None):
        self.coords_x = coords_x
        self.coords_y = coords_y
        self.checker = checker
        self.get_color()


    def get_color(self):
        if (self.coords_x + self.coords_y) % 2 == 0:
            self.color = 'black'
        else:
            self.color = 'white'


    def possible_to_set(self):
        if self.is_free() and self.color == 'black':
            return True
        else:
            return False

    def is_free(self):
        if self.checker == None:
            return True
        else:
            return False


    def set_checker(self, checker):
        self.checker = checker


    def delete_checker(self):
        self.checker = None


    def __str__(self):
        if self.is_free():
            return self.board_dict[self.color]
        elif self.checker.check_queen():
            return self.figure_dict["queen"]
        else:
            return self.figure_dict[self.checker.color]