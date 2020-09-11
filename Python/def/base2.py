# デフォルト値、可変長引数、複数の返り値

from calendar import c


def sample(a,b=10):
    print(a,b)

sample(20,30)
sample(20)

def spam(a,*b):
    print(a,b)
    print(type(b))

spam(10,20,30)

def spam(a,**b):
    print(a,b)
    print(type(b))

spam(10,name=20,age=30)

def sample2():
    return 1,2,3

a,b,c=sample2()

print(a,b,c)