'''Welcome to the Gaurav's world'''
import turtle
turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(1.5)
turtle.pencolor('yellow')

def drawcircle(radius):
    for i in range (12):
        turtle.circle(radius)
        radius=radius-6
def drawdesign():        
    for i in range (16):
        drawcircle(150)
        turtle.right(136)
drawdesign()
turtle.done()