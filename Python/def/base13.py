# map関数

list = [1,2,3,4,5]
map_a = map (lambda x: x*2,list)

for x in map_a:
    print(x)

man = {
    'name':'Ichiro',
    'age':'18',
    'country':'Japan'
}
map_man = map(lambda x: x + ',' + man.get(x), man)

for x in map_man :
    print(x)

def clacurate(x,y,z):
    if z == 'plus':
        return x+y
    if z == 'minus':
        return x-y
    
map_sample = map(clacurate,range(5),[3,3,3,3,3],['plus','minus'])