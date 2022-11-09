# CTI-110-0901
# 11/07/22
# McDonald, Andrew
# P4LAB1c: Snowflake (With Turtle)
#
# Import Turtle
# Adjust Setting
# SET 6 to n
# move to start position
#     draw hexagon with for loop
# move to second position at center
#     draw branches with for loop
#
import turtle
turtle.Screen().bgcolor('#718EBB')
sf = turtle.Turtle()
sf.speed(5)
sf.shape('turtle')
sf.pensize(9)
sf.pencolor('#d5d7d4')
sf.hideturtle()
sf.penup()
sf.goto(30,50)
sf.down()
sf.showturtle()

n = 6

for _ in range(n): # hexagon
    sf.right(360 / n)
    sf.forward(60)

sf.penup()
sf.hideturtle()
sf.goto(0,0)
sf.down()
sf.showturtle()
for i in range(n): # start of branch
    sf.penup()
    sf.hideturtle()
    sf.left(60) # align turtle for first move
    sf.forward(60)
    sf.down()
    sf.showturtle()
    sf.forward(180) # begin branch print outside hex
    sf.back(50)
    sf.left(40)
    sf.forward(45)
    sf.back(45)
    sf.right(80)
    sf.forward(45)
    sf.back(45)
    sf.left(40) # end of first design
    sf.back(50)
    sf.left(40)
    sf.forward(60)
    sf.back(60)
    sf.right(80)
    sf.forward(60)
    sf.back(60)
    sf.left(40) # end of second design
    sf.back(45)
    sf.left(40)
    sf.forward(30)
    sf.back(30)
    sf.right(80)
    sf.forward(30)
    sf.back(30)
    sf.left(40) # end of third design
    sf.penup()
    sf.hideturtle()
    sf.goto(0,0)
# turtle.exitonclick()
#
# END


