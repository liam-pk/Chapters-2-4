import turtle 

turtle.tracer(2)

spiral = turtle.Turtle()

for i in range(300):
    spiral.forward(i * 11)
    spiral.right(144)
    
turtle.done()