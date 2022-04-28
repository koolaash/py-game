import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor("black")
t.speed(-5)
n = 30
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/50
    t.color(c)
    t.left(5)
    for j in range(5):
        t.forward(200)
        t.left(144)
