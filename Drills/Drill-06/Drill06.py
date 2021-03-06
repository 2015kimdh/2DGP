from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global mx, my
    global lx, ly
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx,my = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if SDL_BUTTON_LEFT:
                lx = mx
                ly = my
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def calculate():
    global lx, ly
    global x, y
    if x != lx and y != ly:
        if x > lx:
            x -= 2
        elif x < lx:
            x += 2
        if (ly - y)/(lx - x)*2 > 1 or (ly - y)/(lx - x)*2 < -1:
            y += (ly - y)/(lx - x)
        elif (lx - x) < 1 and (lx - x) >= 0:
            y += 1
        elif (lx - x) > -1 and (lx - x)<= 0:
            y -= 1
    elif x == lx and y == ly:
        pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
lx, ly = 0, 0
mx, my = 0, 0
frame = 0
show_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.01)
    handle_events()
    calculate()
close_canvas()




