from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_to_1():
    x,y = 203, 535
    frame = 0
    while x > 132:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 1
        y -= 4.1
        delay(0.01)
        get_events()

def move_to_2():
    x, y = 132, 243
    frame = 0
    while x < 535:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 1.77
        y += 1
        delay(0.01)
        get_events()

def move_to_3():
    x, y = 535, 470
    frame = 0
    while x > 477:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 1
        y -= 4.6
        delay(0.01)
        get_events()
def move_to_4():
    x, y = 477, 203
    frame = 0
    while x < 715:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 3.55
        y -= 1
        delay(0.01)
        get_events()

def move_to_5():
    x, y = 715, 136
    frame = 0
    while x > 316:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 4.48
        y += 1
        delay(0.01)
        get_events()

def move_to_6():
    x, y = 316, 225
    frame = 0
    while x < 510:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 1.45
        y -= 1
        delay(0.01)
        get_events()

def move_to_7():
    x, y = 510, 92
    frame = 0
    while x < 692:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 1
        y += 2.34
        delay(0.01)
        get_events()

def move_to_8():
    x, y = 692, 518
    frame = 0
    while x > 682:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 0.5
        y -= 9.2
        delay(0.01)
        get_events()

        def move_to_8():
            x, y = 682, 336
            frame = 0
            while x < 712:
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.clip_draw(frame * 100, 0, 100, 100, x, y)
                update_canvas()
                frame = (frame + 1) % 8
                x += 2
                y += 2.6
                delay(0.01)
                get_events()

def move_to_9():
    x, y = 682, 336
    frame = 0
    while x < 712:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 2
        y += 2.6
        delay(0.01)
        get_events()

while True:
    move_to_1()
    move_to_2()
    move_to_3()
    move_to_4()
    move_to_5()
    move_to_6()
    move_to_7()
    move_to_8()
    move_to_9()

close_canvas()
