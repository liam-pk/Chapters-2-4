import turtle
size = 150
def makesquare(turt,size):
    size = 75
    print(size)
    for i in range (4):
        turt.forward(size)
        turt.left(90)
        
wn= turtle.Screen()
sachin = turtle.Turtle()
sachin.color("orange")

andy = turtle.Turtle()


andy.setpos(100,100)

makesquare(andy,150)
makesquare(sachin,200)
print(size)