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
        
    CustomPrint.direct_bypass(A)
    print()
    CustomPrint.symmetric_bypass(A)
    print()
    CustomPrint.reverse_bypass(A)

if __name__ == '__main__':
    
    main()