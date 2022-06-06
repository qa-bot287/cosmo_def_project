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


def turtle_inner_square():
    turtle.shape('turtle')
    r = 20
    turtle.left(45)
    for i in range(10):
        turtle.circle(r, 360, 4)
        turtle.penup()
        turtle.goto(r-r/4, -r+r/4)
        turtle.pendown()
        r = r + 20

# turtle_square()
# turtle_s_draw()
# turtle_circle()
# turtle_inner_square()
