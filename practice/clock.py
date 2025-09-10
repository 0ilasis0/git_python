import datetime
import time
import turtle

now = time.gmtime()

turtle.hideturtle()
turtle.pensize(10)
turtle.pencolor("blue")
turtle.speed(10)
turtle.setup(1500,350,15,50)

#----------------------------------------------------------------基本設定



turtle.penup()
turtle.goto(-700,-135)
turtle.pendown()
year = now[0]
turtle.write('{}年'.format(year),font=("Arial", 18,"normal"))
turtle.penup()
turtle.goto(-700,0)
turtle.pencolor("red")

#----------------------------------------------------------------設定年



def turn_left():
    turtle.left(90)
    turtle.fd(50)
    turtle.pendown()

def forward():
    turtle.fd(50)
    turtle.pendown()

def unit(fly):
    if fly in [0,1,7]:
        turtle.penup()
    forward()
    if fly in [5,6]:
        turtle.penup()
    turn_left()
    if fly in [1,4]:
        turtle.penup()
    turn_left()
    if fly in [1,2,3,7,]:
        turtle.penup()
    turn_left()
    if fly in [1,3,4,5,7,9]:
        turtle.penup()
    forward()
    if fly in [1,4,7]:
        turtle.penup()
    turn_left()
    if fly in [2]:
        turtle.penup()
    turn_left()

def back(distance):
    turtle.penup()
    turtle.bk(distance)
    turtle.pendown()

def next():
    turtle.penup()
    turtle.seth(0)
    turtle.fd(50)
    turtle.pendown()

#----------------------------------------------------------------def定義



addition = 5
dif_addition = 0
temp = []
trans = 0
ok = 0

while True:
    for i in range(addition):
        now_use = now[i+1+dif_addition]
        temp.append(now_use)
        if i == 2 and addition == 5:
            now_use += 8
        elif i == 0 and addition == 3:
            now_use += 8
        elif i == 1 and addition == 4:
            now_use += 8
        elif i == 2 and addition == 5:
            now_use += 8
        ten = now_use//10
        one = now_use%10
        unit(ten)
        next()
        unit(one)
        next()

        turtle.pencolor("blue")
        if i == 0 and ok == 0:
            turtle.write('月',font=("Arial", 18,"normal"))
        elif i == 1 and ok == 0:
            turtle.write('日',font=("Arial", 18,"normal"))
        elif i == 2 and ok == 0:
            turtle.write('時',font=("Arial", 18,"normal"))
        elif i == 3 and ok == 0:
            turtle.write('分',font=("Arial", 18,"normal"))
        elif i == 4 and ok == 0:
            turtle.write('秒',font=("Arial", 18,"normal"))
        turtle.pencolor("red")

        next()
        next()

    back(150)
    ok = 1

#----------------------------------------------------------------更改時間和設定字



    now = time.gmtime()

    if now[1] != temp[0]:   #!=改==能看改動月日時分秒
        renew = 5
    elif now[2] != temp[1]:
        renew = 4
    elif now[3] != temp[2]:
        renew = 3
    elif now[4] != temp[3]:
        renew = 2
    elif now[5] != temp[4]:
        renew = 1
    addition = renew
    dif_addition = 5-renew
    back(150+300*(renew-1))

#----------------------------------------------------------------偵測更改位置



    turtle.pencolor("white")

    for i in range(addition):
        turtle.pendown()
        for j in range(2):
            forward()
            turn_left()
            turn_left()
            turn_left()
            forward()
            turn_left()
            turn_left()
            next()
        next()
        next()

#----------------------------------------------------------------清白更改位置



    if now[1] != temp[0]:       #改==能看改動月日時分秒
        turtle.bk(1500)
        for i in range(5):
            temp[i] = now[i+1]
    elif now[2] != temp[1]:
        turtle.bk(1200)
        for i in range(4):
            temp[i+1] = now[i+2]
    elif now[3] != temp[2]:
        turtle.bk(900)
        for i in range(3):
            temp[i+2] = now[i+3]
    elif now[4] != temp[3]:
        turtle.bk(600)
        for i in range(2):
            temp[i+3] = now[i+4]
    elif now[5] != temp[4]:
        turtle.bk(300)

    turtle.pencolor("red")

#----------------------------------------------------------------回到須改數字位置



    now = time.gmtime()     #從新更新時間



turtle.done()