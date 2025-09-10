import turtle

turtle.setup(1400,700,100,50)
turtle.pensize(3)
turtle.pencolor("blue")
turtle.speed(10)
turtle.hideturtle()
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()



def cal(size, n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0 ,60 ,-120 ,60]:
            turtle.left(angle)
            cal(size/3 ,n-1)




for i in range(3):
    cal(400, 4)
    turtle.right(120)

turtle.done()