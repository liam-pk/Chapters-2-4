import turtle 

turtle.tracer(1) #speed up to 2 for faster tracing

spiral = turtle.Turtle()

for i in range(300):
    spiral.forward(i * 11)
    spiral.right(144)
    
turtle.done()