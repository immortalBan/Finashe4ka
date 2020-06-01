class Branch:
    
    def __init__(self, value=None):
        self.value = value
        self.root = None
        self.left = None
        self.right = None
    
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
    
    def compare(self, key):
        if self.value > key:
            if self.get_left():
                self.left.compare(key)
            else:
                branch = Branch(key)
                self.left = branch
                branch.root = self
        elif self.value < key:
            if self.get_right():
                self.right.compare(key)
            else:
                branch = Branch(key)
                self.right = branch
                branch.root = self
        else:
            raise Exception('Такой элемент уже существует')
    
    def find_to_delete(self, key):
        if self.value == key:
            return self
        elif self.value > key:
            return self.left.find_to_delete(key)
        elif self.value < key:
            return self.right.find_to_delete(key)
    
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
            


class Tree:

    def __init__(self):
        self.root = None

    def push(self, key):
        if self.root:
            self.root.compare(key)
        else:
            self.root = Branch(key)

    def __str__(self):
        return self.root.__str__()
    
    def find_to_delete(self, key):
        return self.root.find_to_delete(key)
    
    def delete(self, key):
        branch_to_delete = self.find_to_delete(key)
        if branch_to_delete.get_left() == None and branch_to_delete.get_right() == None:
            if branch_to_delete.root.right is branch_to_delete:
                branch_to_delete.root.right = None
                branch_to_delete.root = None
            elif branch_to_delete.root.left is branch_to_delete:
                branch_to_delete.root.left = None
                branch_to_delete.root = None
        elif branch_to_delete.get_left() and branch_to_delete.get_right() == None:
            if branch_to_delete.root.right is branch_to_delete:
                branch_to_delete.root.right = branch_to_delete.left
                branch_to_delete.left.root = branch_to_delete.root
            elif branch_to_delete.root.left is branch_to_delete:
                branch_to_delete.root.left = branch_to_delete.left
                branch_to_delete.left.root = branch_to_delete.root
        elif branch_to_delete.get_left() == None and branch_to_delete.get_right():
            if branch_to_delete.root.right is branch_to_delete:
                branch_to_delete.root.right = branch_to_delete.right
                branch_to_delete.right.root = branch_to_delete.root
            elif branch_to_delete.root.left is branch_to_delete:
                branch_to_delete.root.left = branch_to_delete.right
                branch_to_delete.right.root = branch_to_delete.root
        else:
            current = branch_to_delete.right
            while current.left:
                current = current.left
            value = current.value
            self.delete(value)
            branch_to_delete.value = value
            
            
    

class MainClass:
    
    ITEMS = [21, 7, 32, 5, 14, 27, 37, 4, 6, 12, 18, 25, 30, 34, 39, 2, 9, 24, 33]
    ITEMS_TO_ADD = [38, 20, 8, 13, 47]
    ITEMS_TO_DELETE = [33, 14, 5, 32]
    
    def __init__(self):
        tree = Tree()
        for value in self.ITEMS:
            tree.push(value)
        print(tree)
        print('Процесс добавления новых элементов')
        for value in self.ITEMS_TO_ADD:
            tree.push(value)
        print(tree)
        print('Процесс удаления элементов')
        for value in self.ITEMS_TO_DELETE:
            tree.delete(value)
        print(tree)
        
if __name__ == '__main__':
    MainClass()