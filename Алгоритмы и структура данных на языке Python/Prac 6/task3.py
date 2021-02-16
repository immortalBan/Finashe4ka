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
        

class CustomPrint:
    
    @staticmethod
    def direct_bypass(branch):
        if branch:
            print(branch.get_value(), end=' ')
            CustomPrint.direct_bypass(branch.left)
            CustomPrint.direct_bypass(branch.right)
    
    @staticmethod
    def symmetric_bypass(branch):
        if branch:
            CustomPrint.symmetric_bypass(branch.left)
            print(branch.get_value(), end=' ')
            CustomPrint.symmetric_bypass(branch.right)
    
    @staticmethod
    def reverse_bypass(branch):
        if branch:
            CustomPrint.reverse_bypass(branch.left)
            CustomPrint.reverse_bypass(branch.right)
            print(branch.get_value(), end=' ')
            

def main():
    A = Branch('A')
    
    B = A.set_left('B')
    C = A.set_right('C')
    
    D = B.set_left('D')
    E = B.set_right('E')
    F = C.set_right('F')
    
    G = E.set_left('G')
    H = F.set_left('H')
    I = F.set_right('I')
    
    print(A)
    print('Прямой обход')    
    CustomPrint.direct_bypass(A)
    print('\nСимметричный обход')
    CustomPrint.symmetric_bypass(A)
    print("\nОбратный обход")
    CustomPrint.reverse_bypass(A)

if __name__ == '__main__':
    
    main()
