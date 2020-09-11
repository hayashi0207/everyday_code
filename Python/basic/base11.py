car = {'brand':'Toyota','model':'Prius'}
for k,v in car.items():
    print('key = {}, value = {}'.format(k,v))

if 'brand' in car:
    print('carのブランドは{}'.format(car['brand']))

car.update({'country':'Japan'})
car['city']='toyotashi'
print(car)

value=car.popitem()
print(car)
print(value)
value=car.pop('model')
print(car)

del car

# print(car)