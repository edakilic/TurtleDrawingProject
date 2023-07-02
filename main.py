import turtle

drawing_board = turtle.Screen()    #ekran oluşturmak
drawing_board.bgcolor("pink")      #arka plan rengi için #renk kodu da yazılabilir.
drawing_board.title("Python Turtle")   #ekran başlığı
#çizim kısmı aşağısı
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(45)
turtle_instance_2.forward(100)
turtle.done()