# from turtle import *
# import colorsys
# bgcolor("black")
# tracer(41)
# h = 0
# goto(-110, 200)
# for i in range(9999999):
#      c = colorsys.hsv_to_rgb(h, 1, 1)
#      fillcolor(c)
#      begin_fill()
#      lt(119)
#      circle(50)
#      circle(50)
#      circle(20)
#      backward(350 - i)  
#      end_fill()
#      h += 0.005

import turtle

turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("red")


for t in range(4000):
     
     squary.circle(20)
     squary.forward(t)
     squary.left(91)  # Adding this line to create a spiral pattern
