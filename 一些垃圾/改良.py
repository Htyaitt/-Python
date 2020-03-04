import random
secret = random.randint(1,4)
count=3
temp=input("输入一个数字")
guess=int(temp)
while guess!=secret and count>1:
    if guess > secret:
        print("大了")
    if guess < secret:
        print("小了")
    count-=1
    temp = input("你还有"+str(count)+"次机会"+"请重新输入数字:\n")
    guess = int(temp)
if guess == secret:
    print("niubi")
else:
    print("你个哈卵！"+"正确答案是"+str(secret))
        

