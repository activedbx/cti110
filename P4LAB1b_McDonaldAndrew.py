# CTI-110-0901
# 11/05/22
# McDonald, Andrew
# P4LAB1b: Initials (With Turtle)
#
# Import Turtle
# Adjust settings
# Move to start positon and Draw A
# Move to second position and Draw M
#
#
import turtle
turtle.Screen().bgcolor('#79afc5')
crush = turtle.Turtle()
crush.shape('turtle')
crush.speed(3)
crush.pensize(9)
crush.pencolor('#8A9A5B')

# BEGIN
crush.hideturtle()
crush.penup()
crush.goto(-135,100) # to A start position
crush.down()
crush.showturtle()
#
# A
crush.right(60)
crush.forward(200)
crush.penup()
crush.hideturtle()
crush.backward(200)
crush.down()
crush.showturtle()
crush.left(-60)
crush.forward(200)
crush.backward(85)
crush.left(120)
crush.forward(115)

crush.hideturtle()
crush.penup()


crush.goto(5,-73) # to M start position
crush.down()
crush.left(90)
crush.showturtle()
#
# M
crush.forward(173)
crush.right(135)
crush.forward(90)
crush.left(90)
crush.forward(90)
crush.right(135) 
crush.forward(173)
crush.hideturtle()
# turtle.exitonclick()
#
# END
