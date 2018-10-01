from pico2d import *
import random

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def draw_line(p1, p2):

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]

size = 20
points = [(random.randint(-500, 500), random.randint(-400, 350)) for i in range(size)]
n = 1
while True:
    draw_line(points[n-1], points[n])
    n = (n + 1) % size

close_canvas()