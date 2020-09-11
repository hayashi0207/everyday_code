# 高階関数

def print_hello():
    print('hello')

def print_goodbye():
    print('goodbye')

var = ['AA','BB',print_hello,print_goodbye]

var[2]()
var[3]()

def a(msg):
    print(msg)

def b():
    print('こんにちは')

def c(func):
    func('hello')
    return b

var = c(a)
var()