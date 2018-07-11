import turtle 
def draw_name():
    window = turtle.Screen()
    window.bgcolor("red")
    b = turtle.Turtle()
    b.shape( "circle")
    b.speed(1)
    b.color("green")


    b.forward(50)
    b.backward(50)
    b.left(270)
    b.forward(100)
    b.backward(50)
    b.right(270)
    b.forward(50)
    window.exitonclick()
draw_name()