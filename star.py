import turtle

drawing_window = turtle.Screen()
drawing_window.bgcolor("pink")
drawing_window.title("star")

turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(100)

turtle.done()