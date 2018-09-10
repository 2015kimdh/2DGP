from pico2d import*

import math
import os

os.chdir('D:\\GitHub\\2DGP\\Lecture03')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

character.draw_now(400, 90)

way = 0
circle = 0
rx = 400
ry = 360

x = 410
y = 90
angle = 4.7
trigger = 0
grass.draw_now(400, 30)

while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    if(circle == 0):
        if (x <= 800 and way == 0):
            x = x + 10
            character.draw_now(x, y)
            if(x >= 800 and way == 0):
                way = 1
            if(x == 400 and circle == 0 and way == 0):
                circle = 1
                trigger = 1
        elif(y <= 590 and way == 1):
            y = y + 10
            character.draw_now(x, y)
            if(y >= 590 and way == 1):
                way = 2
        elif(x >= 0 and way == 2):
            x = x - 10
            character.draw_now(x, y)
            if(x <= 0 and way == 2):
                way = 3
        elif(y >= 90 and way == 3):
            y = y - 10
            character.draw_now(x, y)
            if(y <= 90 and way == 3):
                way = 0
    elif(circle == 1):
        x = rx + (math.cos(angle)*280)
        y = ry + (math.sin(angle)*280)
        angle = angle + 0.1
        if(x <= 390 and y <= 90):
            circle = 0
            x = 410
            y = 90
            angle = 4.7
        character.draw_now(x, y)

    if(circle == 0):
            delay(0.05)
    elif(circle == 1):
            delay(0.05)


