# セット

s={'a','b','c','d'}
t={'c','d','e'}

u=s|t
# u=s.union(t)
print(u)

u=s&t
# s.intersection(t)
print(u)

u=s-t
# s.difference(t)
print(u)

u=s^t
# s.symmetric_difference(t)
print(u)

s |= t
print(s)

# issubset,issuperset,isdisjoint
s={'apple','banana'}
t={'apple','banana','lemon'}
u={'cherry'}

print(s.issubset(t))
print(t.issuperset(s))
print(t.isdisjoint(s))