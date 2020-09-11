# enumerate,zip,while

from re import A


sample=['A','B','C']
for index, value in enumerate(sample):
    print(index)
    print(value)

classA=['Taro','Hanako','Jiro']
classB=['Katsuo','Wakame','Taro']

for A, B in zip(classA,classB):
    print(A)
    print(B)

count = 0
while count < 10:
    print(count)
    count+=1
    