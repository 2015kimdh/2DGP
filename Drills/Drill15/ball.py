import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(0, 800-1), 0
    def set_center_object(self, boy):
        self.center_object = boy

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        #self.image.draw(self.x, self.y-self.center_object.y)
        self.image.draw(self.dx, self.dy)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        self.dx = clamp(-50, -int(self.center_object.x) + self.x+400,1600)
        self.dy = clamp(-50, -int(self.center_object.y) + self.y+300,800)