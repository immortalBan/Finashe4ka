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
    
    def __str__(self):
        return '{} ({}, {})'.format(self.value, str(self.left), str(self.right))
    
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
        self.expression = result
        
    
    def reverse_polish(self):
        exp = self.expression
        res = []
        stek = []
        for item in exp:
            if item not in self.CHARACTERS:
                res.append(item)
            elif item != ')':
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
    
    def __init__(self):
        while True:
            try:
                raw_expression = input('Введите выражение\n ->')
                expression = Expression(raw_expression)
                break
            except Exception as e:
                print(e)
                print('Попробуйте ввести еще раз')
        print('Результат, полученный с помощью бинарного дерева:\n' + raw_expression, '=', str(expression.get_value()))
        print('Результат, полученный с помощью функции eval():\n' + raw_expression, '=', eval(raw_expression))
    
if __name__ == '__main__':
    MainClass()