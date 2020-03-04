temp = input("请输入一个数")
score = int(temp)
if score > 100 or score<0:
    print("不知道这他妈是百分制？")
    temp = input("重新输入")
    score = int(temp)
if 100 >= score >=90:
    print("A")
elif 90 > score >=80:
    print("B")
elif 80 > score >=70:
    print("C")
elif 70 > score >=60:
    print("D")
elif 60 > score>=0:
    print("你看你真像个废物")
