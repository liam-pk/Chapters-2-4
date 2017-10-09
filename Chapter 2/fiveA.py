import turtle

def drawSpiral(t, angle):

    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2


wn = turtle.Screen()      
wn.bgcolor("lightgreen")

guido = turtle.Turtle()    
guido.color('blue')

guido.penup()
guido.backward(110)
guido.pendown()

drawSpiral(guido, 90)


