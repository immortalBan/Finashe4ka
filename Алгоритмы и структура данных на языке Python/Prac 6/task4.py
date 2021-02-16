import timeit

class Branch:
    
    def __init__(self, value=None, index=None):
        self.value = value
        self.index = index
        self.root = None
        self.left = None
        self.right = None
    
    def __str__(self):
        return '{} ({}, {})'.format((self.value, self.index), str(self.left), str(self.right))
    
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
    
    def set_right(self, new_value):
        branch = Branch(new_value)
        self.right = branch
        branch.root = self
        return branch
    
    def set_left(self, new_value):
        branch = Branch(new_value)
        self.left = branch
        branch.root = self
        return branch
    
    def compare(self, key, index):
        if self.value > key:
            if self.get_left():
                self.left.compare(key, index)
            else:
                branch = Branch(key, index)
                self.left = branch
                branch.root = self
        elif self.value < key:
            if self.get_right():
                self.right.compare(key, index)
            else:
                branch = Branch(key, index)
                self.right = branch
                branch.root = self
        else:
            raise Exception('Такой элемент уже существует')
    
    def find(self, key):
        if self.value == key:
            return self.index
        elif self.value > key:
            return self.left.find(key)
        elif self.value < key:
            return self.right.find(key)
            


class Tree:

    def __init__(self):
        self.root = None
        self.len = 0

    def push(self, key, index):
        if self.root:
            self.root.compare(key, index)
        else:
            self.root = Branch(key, index)
        self.len = index + 1

    def __str__(self):
        return self.root.__str__()
    
    def find(self, key):
        try:
            return self.root.find(key)
        except AttributeError:
            ans = input('Такого элемента не существует\nХотите добавить? y/n\n ->')
            if ans == 'y':
                self.push(key, self.len)
                return self.root.find(key)
    

class MainClass:
    
    ITEMS = [81, 77, 79, 68, 10, 12, 13, 20, 15, 24, 27, 42, 33, 51, 57]
    
    def __init__(self):
        tree = Tree()
        for index, value in enumerate(self.ITEMS):
            tree.push(value, index)
        print(tree)
        
        while True:
            try:
                item_to_find = int(input('Введите число для поиска\n ->'))
                break
            except:
                continue
        
        a = timeit.default_timer()
        index_1 = tree.find(item_to_find)
        time_1 = timeit.default_timer() - a
        a = timeit.default_timer()
        index_2 = self.ITEMS.index(item_to_find)
        time_2 = timeit.default_timer() - a
        new_ITEMS = sorted(self.ITEMS)
        a = timeit.default_timer()
        index_3 = new_ITEMS.index(item_to_find)
        time_3 = timeit.default_timer() - a
        
        print(f'Результат поиска по бинарному дереву:\n {index_1}\nЭто заняло {time_1} секунд')
        print(f'Результат поиска по списку:\n {index_2}\nЭто заняло {time_2} секунд')
        print(f'Результат поиска по отсортированному списку:\n {index_3}\nЭто заняло {time_3} секунд')
        
        
        
if __name__ == '__main__':
    MainClass()