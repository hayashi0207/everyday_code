# タプル

fruit = ('apple','banana','lemon')
print(fruit)
print(type(fruit))
print(fruit[0])
fruit = fruit + ('grape',)
print(fruit)

list_fruit = ['orange','water-melon']
fruit = tuple(list_fruit)
print(fruit)
print(fruit.count('orange'))
print(fruit.index('orange'))

pos = (135,35)

countries = {pos:'Japan'}

print(countries.get((135,35)))