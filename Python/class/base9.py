from abc import abstractmethod, ABCMeta

class Human(metaclass=ABCMeta):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(self.name)

class Woman(Human):
    def say_something(self):
        print(f'女性名：{self.name}')

class Man(Human):
    def say_something(self):
        print(f'男性名：{self.name}')


gender = input('男性：1、女性：2')
if gender=='1':
    human = Woman('hanako')
elif gender=='2':
    human = Man('taro')
else:
    print('入力が間違っています')
human.say_something()