import operator

class Tree:
    
    def __init__(self, root):
        self.root = root
        self.value = self.processing(self.root)
    
    def processing(self, token):
        operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    
        left_value = token.get_left()
        right_value = token.get_right()
    
        if left_value and right_value:
            fn = operators[token.value]
            return fn(self.processing(token.left),self.processing(token.right))
        else:
            return int(token.value)
    
    def __str__(self):
        return str(self.root)
    
    def get_value(self):
        return self.value
        
class Branch:
    
    def __init__(self, value=None):
        self.value = value
        self.root = None
        self.left = None
        self.right = None
    
    def tree_string(self, root, curr_index, index=False, delimiter='-'):
        """Красивое дерево"""
        
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
        else:
            node_repr = str(root.value)

        new_root_width = gap_size = len(node_repr)

        l_box, l_box_width, l_root_start, l_root_end = \
            self.tree_string(root.left, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            self.tree_string(root.right, 2 * curr_index + 2, index, delimiter)


        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), new_root_start, new_root_end

    def __str__(self):
        """Вывод структуры на экран"""

        lines = self.tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))
    
    def get_value(self):
        return self.value
    
    def get_left(self):
        if self.left:
            return self.left.value
        else:
            return None
    
    def get_right(self):
        if self.right:
            return self.right.value
        else:
            return None

class Expression:
    
    CHARACTERS = '+-/*()'
    
    def __str__(self):
        return str(self.tree)
    
    def __init__(self, expression):
        self.expression = expression
        self.process_data()
        if self.is_correct_data():
            self.reverse_polish()
            self.tree_constructor()
            self.tree = Tree(self.root)
        
    def get_value(self):
        return self.tree.get_value()
        
    def is_correct_data(self):
        exp = self.expression
        characters = marks = brackets_left = brackets_right = 0
        for item in exp:
            if item not in self.CHARACTERS:
                marks += 1
            elif item == '(':
                brackets_left += 1
            elif item == ')':
                brackets_right += 1
            elif item in self.CHARACTERS:
                characters += 1
            else:
                raise Exception('Неизвестный знак')
        if brackets_left > brackets_right:
            raise Exception('Не хватает правых скобок')
        elif brackets_left < brackets_right:
            raise Exception('Не хватает левых скобок')
        elif marks > characters + 1:
            raise Exception('Слишком много чисел')
        elif marks < characters + 1:
            raise Exception('Слишком много алгебраических знаков')
        else:
            return True

    def process_data(self):
        exp = self.expression.replace(' ', '')
        result=[]
        temp=''
        for item in exp:
            if item not in self.CHARACTERS:
                temp += item
            else:
                if len(temp)!=0:
                    result.append(temp)
                    temp = ''
                result.append(item)
        if len(temp)!=0:
            result.append(temp)
        self.expression = result
        
    
    def reverse_polish(self):
        exp = self.expression
        res = []
        stek = []
        for item in exp:
            if item not in self.CHARACTERS:
                res.append(item)
            elif item != ')':
                if item in '+-':
                    if len(stek) == 0 or stek[-1] not in '*/':
                        stek.append(item)
                    else:
                        res += stek[::-1]
                        stek = []
                        stek.append(item)
                else:
                    stek.append(item)
            else:
                index = ''.join(stek).rindex('(')
                res += stek[index+1:][::-1]
                stek = stek[:index]
        if len(stek)!=0:
            res += stek[::-1]
        self.expression = res

    def tree_constructor(self):
        exp = self.expression
        new_stek = []
        for item in exp:
            if item not in self.CHARACTERS:
                obj = Branch(item)
                new_stek.append(obj)
            else:
                obj = Branch(item)
                new_stek[-1].root = obj
                new_stek[-2].root = obj
                obj.left = new_stek[-2]
                obj.right = new_stek[-1]
                new_stek = new_stek[:-2]
                new_stek.append(obj)
        self.root = new_stek[0]

class MainClass:
    
    EXPRESSION_LIST = [
            '2+2',
            '(2+3)*4',
            '(7+8)*(2-1)',
            '(7+8)*(2-1)+7',
            '(7+8)*(5-2)/(2-1)'
            ]
    
    def __init__(self):
        for exp in self.EXPRESSION_LIST:
            expression = Expression(exp)
            print(expression)
            print('Результат, полученный с помощью бинарного дерева:\n' + exp, '=', str(expression.get_value()))
            print('Результат, полученный с помощью функции eval():\n' + exp, '=', eval(exp))
        
        while True:
            try:
                raw_expression = input('Введите выражение\n ->')
                expression = Expression(raw_expression)
                break
            except Exception as e:
                print(e)
                print('Попробуйте ввести еще раз')
        print(expression)
        print('Результат, полученный с помощью бинарного дерева:\n' + raw_expression, '=', str(expression.get_value()))
        print('Результат, полученный с помощью функции eval():\n' + raw_expression, '=', eval(raw_expression))
    
if __name__ == '__main__':
    MainClass()
