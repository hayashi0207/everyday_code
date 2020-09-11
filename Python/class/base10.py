# プライベート変数


class Human:

    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_msg(self):
        print(self.__name)

human = Human('taro', 15)
# print(human.__name)

human.print_msg()
