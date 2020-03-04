import random
secret = random.randint (1,10)
count=4
tamp = input("请输入一个数")
guess = int(tamp)
while guess != secret and count > 1:
    if guess < secret:
        print("小了")
    if guess > secret:
        print("大了")
    count-=1
    tamp = input("你还有"+str(count)+"次机会请重新输入")
    guess = int(tamp)
if guess == secret:
    print("弔人")
else:
    print("你个垃圾"+"是"+str(secret))
    
