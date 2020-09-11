# ジェネレータ関数

def a(max):
    print('ジェネレータ作成')
    for n in range(max):
        x = yield n
        print(x)
        print('実行')

gen = a(10)
next(gen)
gen.send(100)
# gen.throw(ValueError())
gen.close()
# for x in gen:
#     print(x)
# n = next(gen)
# print(n)
# n = next(gen)
# print(n)