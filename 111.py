import random

d=(int(input("只能猜幾次")))

b=0

c=0

X=(int(input("數字下限")))

y=(int(input("數字上限")))

n=(random.randint(X,y))

for i in range((y-X+1)):

    if c==d:

        break

    a=(int(input("enter a number")))

    if a!=n:

        if a>n:

            print("太大")

            c=c+1

        else:

            print("太小")

            c=c+1

    else:

        print("正確")

        c=c+1

        b=1