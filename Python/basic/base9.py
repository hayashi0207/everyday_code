# 配列 ,append,extend,insert,remove,pop,count,index
from audioop import reverse


values=['a',['b','c'],'c','d','e','f']
print(values[-1])
print(values[1][1])
print(values[2:])
print(values[3:6])
values.append('apple')
print(values)
values.append(['banana','melon'])
print(values)
values.extend(['banana','melon'])
print(values)
values.insert(1,'grape')
print(values)
values.remove('c')
print(values)
values.pop()
print(values)
print(values.count('a'))
print(values.index('e'))
print(values)

#copy,sort,reverse,clear
print(values)
values_cp=values.copy()
values_cp[0]='AAAAA'
print(values)

print(values)
values_cp=values
values_cp[0]='AAAAA'
print(values)

values=[1,4,3,2,5]

values=sorted(values)
print(values)
values.reverse()
print(values)

values.clear()
print(values)
