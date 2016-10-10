import turtle
import math

window = turtle.Screen()
window.bgcolor("black")

def draw_square(some_turtle):

    some_turtle.shape("triangle")
    some_turtle.color("green")
    some_turtle.speed(6)
    
    count = 0
    while (count < 4):
        some_turtle.forward(100)
        some_turtle.right(90)
        count += 1
    
def draw_circle(some_turtle):
    some_turtle.shape("arrow")
    some_turtle.color("blue")
    some_turtle.circle(100)
    
def draw_triangle(some_turtle):
    some_turtle.shape("turtle")
    some_turtle.color("red")
    
    some_turtle.forward(150)
    some_turtle.left(90)
    some_turtle.forward(150)
    some_turtle.left(135)
    some_turtle.forward(150*math.sqrt(2))

brad = turtle.Turtle()
angie = turtle.Turtle()
jack = turtle.Turtle()
for i in range(1,37):
    draw_square(brad)
    brad.right(10)
#draw_circle(angie)
#draw_triangle(jack)
window.exitonclick()