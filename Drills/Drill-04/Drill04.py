from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
side = 0

while (1):
    clear_canvas()
    grass.draw_now(400,30)
    if side == 0:
       character.clip_draw(frame * 100,100,100,100, x, 90)
       update_canvas()
       frame = (frame + 1) % 8
       x += 5
    elif side == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5

    if x > 800:
        side = 1
    elif x < 0:
        side = 0
    delay(0.01)
    get_events()

close_canvas()

