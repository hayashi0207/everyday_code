# サブジェネレータ

def sub_sub_generator():
    yield "Sub Subのyield"
    return "sub subのreturn"

def sub_generator():
    yield "subのyield"
    res = yield from sub_sub_generator()
    print(res)
    return "subのreturn"

def generator():
    yield "yield"
    res = yield from sub_generator()
    print(res)
    return "return"

gen=generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))