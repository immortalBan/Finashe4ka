import CheckerClass
import const

class Bool:

    def correct_coords(coords_x, coords_y, color=None):
        NUM = [1, 2, 3, 4, 5, 6, 7, 8, '1', '2', '3', '4', '5', '6', '7', '8']
        ALPH = list('abcdefgh')
        if (coords_x in ALPH or coords_x in NUM) and coords_y in NUM:
            if color:
                if type(coords_x) == str:
                    try:
                        coords_x = const.main_dict[coords_x]
                    except:
                        coords_x = int(coords_x)
                if type(coords_y) == str:
                    coords_y = int(coords_y)
                coords_x -= 1
                coords_y -= 1
                checker = CheckerClass.Checker(color, coords_x, coords_y)
                return not checker.check_queen()
            else:
                return True
        else:
            return False
