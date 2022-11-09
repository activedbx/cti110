# CTI-110-0901
# 11/05/22
# McDonald, Andrew
# P4LAB1a: Shapes (With Turtle)
#
# Import Turtle
# Adjust settings
# Move to start position
#    Draw Triangle with for loop
# Move to second position
#    Draw Square with for loop
#
import turtle
turtle.Screen().bgcolor('#79afc5')
crush = turtle.Turtle()
crush.speed(3)
crush.shape('turtle')
crush.pensize(9)
crush.pencolor('#8A9A5B')

# BEGIN
crush.penup()
crush.hideturtle()
crush.goto(-50,-40) # to Triangle start position
crush.down()
crush.showturtle()
#Triangle
for _ in range(3):
    crush.left(120)
    crush.forward(150)
    
crush.penup()
crush.hideturtle()
crush.goto(150,-40) # to Square start position
crush.down()
crush.showturtle()
# Square
for _ in range (4):
    crush.left(90)
    crush.forward(130)

crush.hideturtle()
# turtle.exitonclick()
#
# END


