import turtle

drawing_window = turtle.Screen()
drawing_window.bgcolor("light green")
drawing_window.title("shrinking star")

turtle_instance = turtle.Turtle()
turtle_instance.color("purple")

def shrinkingsquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingsquare(150)
shrinkingsquare(120)
shrinkingsquare(90)
shrinkingsquare(60)
shrinkingsquare(30)

turtle.done()