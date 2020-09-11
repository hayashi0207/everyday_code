# グローバル関数

def printAnimal():
    animal='Cat'
    print('関数内animal={}, id={}'.format(animal,id(animal)))

animal='dog'
printAnimal()
print(animal,id(animal))