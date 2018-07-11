import turtle 



def drawing():
    window = turtle.Screen()
    window.bgcolor("red")
    b = turtle.Turtle()
      #drawwing square
    b.shape( "circle")
    b.speed(20)
    b.color("green")
    i = 0 
    angle = 20.05 
    while i < 50:
        j = 0
        b.right(angle)
        
        while j < 2:
            b.right(30)
            b.forward(100)
            b.right(150)
            b.forward(100)
            j = j + 1
        i = i + 1
    while i < 100:
        j = 0
        b.right(angle)
        while j < 2:
            b.right(90)
            b.forward(100)
            b.right(90)
            b.forward(100)
            j = j + 1
        i = i + 0.3
    
       
        
    b.right(90)
    b.forward(200)
    window.exitonclick()
drawing()