import turtle

def drawMyInitials():
    window = turtle.Screen()
    window.bgcolor("black")
    chan = turtle.Turtle()
    chan.color("green")
    chan.speed(2)
    chan.right(180)
    chan.circle(90,180)
    chan.penup()
    chan.forward(180)
    chan.left(90)
    chan.pendown()
    chan.forward(180)
    chan.right(90)
    chan.forward(90)
    chan.right(180)
    chan.forward(180)
    
    window.exitonclick()
    
drawMyInitials()