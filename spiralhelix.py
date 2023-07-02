import turtle

turle_window = turtle.Screen()
turle_window.bgcolor("black")
turle_window.title("spiral helix")

turtle_instance = turtle.Turtle()
turtle_instance.color("purple")

turtle_colors = ["pink", "green", "blue", "red", "purple", "light yellow"]

for i in range(10):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i * 2)

turtle.done()