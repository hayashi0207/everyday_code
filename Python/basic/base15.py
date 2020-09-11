# if文

class ClassA():

    def __init__(self,a):
        self.a = a

    def __bool__(self):
        if self.a == 'a':
            return True
        return False

var = ClassA('a')

if var:
    print('true')