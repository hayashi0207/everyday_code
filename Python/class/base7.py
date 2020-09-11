# クラスの多重継承

class ClassA:
    def __init__(self,name):
        self.a_name = name

    def print_a(self):
        print(f'クラスA:{self.a_name}')

class ClassB:
    def __init__(self,name):
        self.b_name = name

    def print_b(self):
        print(f'クラスB:{self.b_name}')

class NewClass(ClassA,ClassB):
    def __init__(self,a_name,b_name,name):
        ClassA.__init__(self,a_name)
        ClassB.__init__(self,b_name)
        self.name=name

    def print_new(self):
        ClassA.print_a(self)
        ClassB.print_b(self)
        
sample = NewClass('Aname','Bname','names')
sample.print_new()

