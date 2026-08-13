import turtle

t = turtle.Turtle()
t.speed(0)
for _ in range(90):
    t.left(50)
    t.forward(2)
    t.circle(50, 200)
    t.right(1)
    t.circle(50, 200)
    t.forward(2)
turtle.done()