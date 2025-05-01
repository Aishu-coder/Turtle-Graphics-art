# import colorgram
# colors=colorgram.extract("imaged18.jpg",20)
# rgb_color=[]
# for color in colors :
#      r=color.rgb.r
#      g=color.rgb.g
#      b=color.rgb.b
#      new=(r,g,b)
#      rgb_color.append(new)
# print(rgb_color)
import random
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
turtle.colormode(255)
t.hideturtle()
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71),
              (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229),
              (14, 205, 222), (63, 21, 10), (224, 19, 111)]
t.penup()
t.speed('fastest')
t.setheading(225)
t.fd(315)
t.setheading(0)
for i in range(10):
    for j in range(10):
        t.forward(50)
        t.dot(20, random.choice(color_list))
    t.setheading(90)
    t.fd(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)

screen.exitonclick()
