# 文字列型
fruit = 'apple'
print(fruit*10)

fruits="""apple
banana
orange
"""
print(fruit[3])

fruit = 'apple'
byte_fruit=fruit.encode('utf-8')
print(type(byte_fruit))
str_fruit=byte_fruit.decode('utf-8')
print(type(str_fruit))

# count
msg = "ABCDEABC"
print(msg.count('ABC'))

#startswith, endswith

print(msg.startswith("ABCD"))
print(msg.endswith("ABCD"))

# strip(両端),rstrip(右端),lstrip(左端)

msg = ' ABC '
print(msg.strip())
print(msg.strip('C'))

msg = 'ABCDEFABC'
print(msg.strip('BAC'))

# upper,lower,swapcase,replace,capitalize

msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u,msg_l,msg_s)

print(msg.replace('ABC',"FFF"))

print(msg.capitalize())

#文字列の一部取り出し
msg = 'hello,my name is taro'
print(msg[:5])
print(msg[5:])
print(msg[6:13])
print(msg[1:10:2])

name='taro'
print('hello{}'.format(name))
print(f'hello{name}')#3.6

msg = 'apPle'
print(msg.islower())
print(msg.isupper())

# find,index,rfind,rindex

msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind( 'ABC' ))
print(msg.index('ABCE'))
print(msg.rindex( 'ABC' ))