import turtle


# Нарисовать букву S (Упражнение 2)
def turtle_s_draw():
    turtle.shape('turtle')
    turtle.delay(150)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


# Нарисовать квадрат (Упражнение 3)
def turtle_square():
    turtle.shape('turtle')
    turtle.delay(150)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)


# Нарисовать окружность (Упражнение 4)
def turtle_circle():
    turtle.shape('turtle')
    turtle.circle(100)


# Нарисовать вложенные квадраты (Упражнение 5)
def turtle_inner_square():
    turtle.shape('turtle')
    r = 20
    turtle.left(45)
    for i in range(10):
        turtle.circle(r, 360, 4)
        turtle.penup()
        turtle.goto(r - r / 4, -r + r / 4)
        turtle.pendown()
        r = r + 20


# Нарисовать паука, где n = 12 (Упражнение 6)
def turtle_spider():
    turtle.shape("turtle")
    turtle.goto(0, 0)

    n = 12

    for i in range(n):
        turtle.forward(150)
        turtle.stamp()
        turtle.left(360)
        turtle.backward(150)
        turtle.left(360)
        turtle.right(360 / n)


# turtle_square()
# turtle_s_draw()
# turtle_circle()
# turtle_inner_square()
# turtle_spider()
