import random

print(random.randint(0,9))

#猜数字

i = 1
a = random.randint(0,100)
b = int(input('请输入0-100之间的数字'))

while a != b:
    if a > b:
        print('你第%d次猜的数字偏小，请再次输入'%i)
        b = int(input())

    else:
        print('你第%d次猜的数字偏大，请再次输入'%i)
        b = int(input())
    
    i+=1

else:
    print('你猜对了')
