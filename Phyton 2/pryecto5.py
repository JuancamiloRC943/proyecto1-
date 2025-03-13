import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return (12 * math.cos(k) - 5 * math.cos(2 * k) - 
            2 * math.cos(3 * k) - math.cos(4 * k))

def draw_heart(x, y, size, text=None, text_size=18):
    """ Dibuja un corazón en la posición (x, y) con un tamaño determinado. """
    color("red")  
    penup()
    goto(x + hearta(0) * size, y + heartb(0) * size)
    pendown()
    for i in range(100):
        k = i * 2 * math.pi / 100
        goto(x + hearta(k) * size, y + heartb(k) * size)
    penup()
    
    if text:
        goto(x, y - size * 1.8)  
        color("white")
        write(text, align="center", font=("Arial", text_size, "bold"))
    pendown()

speed(0)
bgcolor("black")
color("red")
pensize(8)

draw_heart(0, 0, 20)

penup()
goto(0, -50)
color("white")
write("Te amo Catalina", align="center", font=("Brush Script MT", 45, "bold"))

draw_heart(-180, 100, 4, "C + J", text_size=14)  
draw_heart(180, 100, 4, "C + J", text_size=14)  

hideturtle()
done()
