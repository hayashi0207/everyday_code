# name = input('名前を入力してください。')
# print(f'入力された名前は{name}です。')

# # 2進数なので3
# num1 = 0b11
# # 8進数なので9
# num2 = 0o11
# # 16進数なので17
# num3 = 0x11

# print(bin(3))
# print(oct(9))
# print(hex(17))

# array_a = [1,2,3,4,5,6,7,8,9]
# print(array_a[2:9])
# # [インデックスの最初:最後＋1]
# print(array_a[0:9:3])
# print(array_a[-2:])

list_a = []
list_b = [1,2,3]

while len(list_a)<=2:
    a = input("文字列を入力してください。")
    list_a.append(a)
    print(list_a)

list_a.extend(list_b)
print(list_a)