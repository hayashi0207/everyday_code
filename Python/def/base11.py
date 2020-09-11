# リスト内包表記

list_a = (1,2,3,4,5,6,19,'a')

list_b = [x for x in list_a if type(x)==int]
print(list_b)

list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)

dict_a = {
    'a':'Apple',
    'b':'Banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x)==str]
print(list_c)