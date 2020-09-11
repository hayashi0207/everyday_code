# クラスの継承 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greeting(self):
        print(self.name) 
    
    def say_age(self): 
        print(self.age)
    
class Employee(Person):

    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number = number

    def say_number(self, number):
        print(self.number)

    def gretting(self):
        super().greeting()
        print(self.number)

man= Employee('Tonegawa',45,'08040000000')
man.gretting()