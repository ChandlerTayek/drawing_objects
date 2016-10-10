import turtle
import math

window = turtle.Screen()
window.bgcolor("black")

def draw_square():
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("green")
    brad.speed(3)
    
    count = 0
    while (count < 4):
        brad.forward(100)
        brad.right(90)
        count += 1
    
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
def draw_triangle():
    jack = turtle.Turtle()
    jack.shape("turtle")
    jack.color("red")
    
    jack.forward(150)
    jack.left(90)
    jack.forward(150)
    jack.left(135)
    jack.forward(150*math.sqrt(2))
    
    window.exitonclick()
    
draw_square()
draw_circle()
draw_triangle()