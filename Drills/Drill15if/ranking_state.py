import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state

from boy import Boy
from zombie import Zombie


boy = None


name = "Rankingstate"


def enter():
    hide_cursor()
    hide_lattice()

def exit():
    pass

def pause():
    pass

def resume():
    pass

def get_boy():
    return boy

    # fill here


def save_rank():
    import operator
    return tuple(sorted(ranking.items(), key=operator.itemgetter(0)))
    with open('rank.sav', 'w')as f:
        ranking_string = json.dumps(ranking)
    # fill here


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_state(world_build_state)

def update():
    pass

def draw():
    clear_canvas()
    update_canvas()

ranking = [
          {"time" : 0},
          {"time" : 0},
          {"time" : 0},
          {"time" : 0},
          {"time" : 0},
          {"time" : 0},
          {"time" : 0},
          {"time" : 0},
          {"time" : 0},
          {"time" : 0}
        ]





