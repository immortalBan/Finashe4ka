import TableClass
import const
import BoolClass
import CheckerClass
import random as rd

class Game:
    
    def __init__(self):
        self.user = 'white' if input('Выберите цвет шашек:\n1. Светлые\n2. Тёмные\n ->') == '1' else 'black'
        self.table = TableClass.Table()
        self.moves_list = []
        self.table.auto_fill() if input('Выберите способ заполнения доски:\n1. Автоматический\n2. Ручной\n ->') == '1' else self.table.manual_fill()
        self.print_table()
        self.game()
        self.print_game_over()
        

    def game(self):
        self.turn_flag = True if self.user == 'white' else False
        gameOver = self.game_over()
        while not gameOver:
            if self.turn_flag:
                self.user_move()
                self.turn_flag = False
            else:
                self.ai_move()
                self.turn_flag = True
            print('Совершён ход ' + self.moves_list[-1])
            self.print_table()
            gameOver = self.game_over()
    
    def game_over(self):
        if len(self.find_moves('white')) == 0 and self.turn_flag or len(self.find_moves('black')) == 0 and not self.turn_flag:
            return True
        elif self.check_queen():
            return True
        elif not self.check_checkers():
            return True
        else:
            return False
    
    def check_checkers(self):
        white_count = 0
        black_count = 0
        for x in range(8):
            for y in range(8):
                if not self.table.table[y][x].is_free():
                    if self.table.table[y][x].checker.color == 'white':
                        white_count += 1
                    else:
                        black_count += 1
        return bool(min(1, min(white_count, black_count)))
    
    def check_queen(self):
        for x in range(8):
            for y in range(8):
                if not self.table.table[y][x].is_free():
                    if self.table.table[y][x].checker.check_queen():
                        return True
        return False
    
    def print_table(self):
        print(self.table)
    
    def find_moves(self, color):
        possible_moves_fight = []
        possible_moves_peace = []
        for x in range(8):
            for y in range(8):
                if not self.table.table[y][x].is_free() and self.table.table[y][x].checker.color == color:
                    for i in range(len(const.moves_fight)):
                        new_x = x + const.moves_fight[i][0]
                        new_y = y + const.moves_fight[i][1]
                        if BoolClass.Bool.correct_coords(new_x + 1, new_y + 1):
                            if self.table.table[new_y][new_x].is_free():
                                enemy_x = x + const.opponent_fight[i][0]
                                enemy_y = y + const.opponent_fight[i][1]
                                if not self.table.table[enemy_y][enemy_x].is_free():
                                    if self.table.table[enemy_y][enemy_x].checker.color != color:
                                        old_x = const.reverced_main_dict[x+1]
                                        old_y = str(y+1)
                                        new_x = const.reverced_main_dict[new_x+1]
                                        new_y = str(new_y+1)
                                        possible_moves_fight.append(old_x + old_y + ":" + new_x + new_y)
                    for move in const.moves_peace[color]:
                        new_x = x + move[0]
                        new_y = y + move[1]
                        if BoolClass.Bool.correct_coords(new_x + 1, new_y + 1):
                            if self.table.table[new_y][new_x].is_free():
                                old_x = const.reverced_main_dict[x+1]
                                old_y = str(y+1)
                                new_x = const.reverced_main_dict[new_x+1]
                                new_y = str(new_y+1)
                                possible_moves_peace.append(old_x + old_y + "-" + new_x + new_y)
        if len(possible_moves_fight) != 0:
            return possible_moves_fight
        else:
            return possible_moves_peace
    
    def user_move(self):
        color = self.user
        possible_moves = self.find_moves(color)
        while True:
            input_move = input('Введите ход\n ->')
            if input_move in possible_moves:
                self.make_move(input_move)
                break
            else:
                print('Такой ход не может быть совершён. Попробуйте еще раз')
                print('Пример хода, который может быть совершён: ' + rd.choice(possible_moves))
    
    def ai_move(self):
        color = 'black' if self.user == 'white' else 'white'
        possible_moves = self.find_moves(color)
        possible_moves = sorted(possible_moves, key = lambda x: x[-1], reverse=False if color=='black' else True)
        self.make_move(possible_moves[0])
    
    def make_move(self, move):
        if move[2] == ':':
            x = const.main_dict[move[0]] - 1
            y = int(move[1]) - 1
            new_x = const.main_dict[move[3]] - 1
            new_y = int(move[4]) - 1
            color = self.table.table[y][x].checker.color
            self.table.table[y][x].delete_checker()
            self.table.table[(y + new_y)//2][(x + new_x)//2].delete_checker()
            self.table.table[new_y][new_x].set_checker(CheckerClass.Checker(color, new_x, new_y))
        else:
            x = const.main_dict[move[0]] - 1
            y = int(move[1]) - 1
            new_x = const.main_dict[move[3]] - 1
            new_y = int(move[4]) - 1
            color = self.table.table[y][x].checker.color
            self.table.table[y][x].delete_checker()
            self.table.table[new_y][new_x].set_checker(CheckerClass.Checker(color, new_x, new_y))
        self.moves_list.append(move)
    
    
    def print_game_over(self):
        print('Конец игры')
        if len(self.moves_list)%2 == 0 and self.user == 'black' or len(self.moves_list)%2 == 1 and self.user == 'white':
            print('Вы выиграли')
        else:
            print('Вы проиграли')
        print('Вот запись игры:')
        i = 0
        while True:
            try:
                if i%2 == 0:
                    print('\n', i//2 + 1, self.moves_list[i], end=' ')
                else:
                    print(self.moves_list[i], end='')
                i+=1
            except:
                print('X')
                break
            