from pico2d import *
import random

open_canvas()

kpu = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

def make_line(p1, p2):
    frame = 0
    clear_canvas_now()
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        kpu.draw_now(300, 100)
        if p2[0] - p1[0] > 0:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else :
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame += 1
        frame = frame % 8
        delay(0.01)
        get_events()


size = 20
points = [(random.randint(100, 700), random.randint(100, 600)) for i in range(size)]
n = 1


while True:

    make_line(points[n-1], points[n])
    n = (n + 1) % size


close_canvas()