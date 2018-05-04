import turtle
import winsound

def draw_sun():
    window = turtle.Screen()
    window.bgcolor("red")

    pen = turtle.Turtle()

    pen.shape("classic")
    pen.color("yellow")
    pen.speed(10)
    squares = 0
    
    while squares < 20: 
        count = 0
        while count < 4:
            pen.forward(100)
            pen.right(90)
            count += 1
        pen.right(18)
        squares += 1
    window.exitonclick()

draw_sun()
