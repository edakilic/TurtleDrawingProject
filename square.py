import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")
drawing_board.title("square")

turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle.done()

##short way##

import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")
drawing_board.title("square")

turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)

turtle.done()
