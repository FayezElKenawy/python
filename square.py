import turtle
def drawing():
    window = turtle.Screen()
    window.bgcolor("red")
    b = turtle.Turtle()
      #drawwing square
    b.shape( "circle")
    b.speed(1)
    b.color("green")
    i = 0 
    while i < 2:
         b.right(30)
         b.forward(100)
         b.right(150)
         b.forward(100)
         i = i + 1
    b.backward(100)
    while i < 2:
         b.right(150)
         b.forward(100)
         b.right(30)
         b.forward(100)
         i = i + 1
   
    window.exitonclick()
drawing()  
    #drawwing circle
"""cir = turtle.Turtle()
   cir.shape("arrow")
   cir.color("blue")
   cir.speed(2)
   cir.circle(100)
   #drawwing triangle
   tri = turtle.Turtle()
   tri.shape("turtle")
   tri.color("black")
   tri.speed(5) 
   tri.left(60)
   tri.forward(100) 
   tri.right(120)
   tri.forward(100)  
   tri.right(120)
   tri.forward(100) """    
 
    