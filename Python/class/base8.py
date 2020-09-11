# メタクラス

class MetaException(Exception):
    pass

class Meta1(type):

    def __new__(metacls, name, bases, class_dict):    
        print(metacls)
        print(name)
        print(bases)
        print(class_dict)
        if 'my_var' not in class_dict.keys():
            raise MetaException('my_varを定義してください')        
        return super().__new__(metacls,name,bases,class_dict)

class ClassA(metaclass=Meta1):
    a='123'
    pass


    