import pyglet
from pyglet import image
from pyglet.gl import *

from modules.flakes.files import thing, load, resources
from collections import namedtuple
import random

# Set up a window
# myWindow = namedtuple('myWindow', ['X', 'Y'])
# myWin = myWindow(800, 600)
# game_window = pyglet.window.Window(myWin.X, myWin.Y, visible=False, resizable=False)
# counter = pyglet.window.FPSDisplay(window=game_window)

# main_batch = pyglet.graphics.Batch()

# Global Wind
globalVx = 0.0

game_objects = []

# We need to pop off as many event stack frames as we pushed on
# every time we reset the level.
event_stack_size = 0

def init(main_batch, myWin):
    global num_things, fgpic, fgpicSprite, bgpic, bgpicSprite, globalVx

    # Set up the top label
    level_label = pyglet.text.Label(text="Flakes!", x=400, y=575, anchor_x='center', batch=main_batch)

    #print('Flake:init()')
    num_things = 30
    fgpic = pyglet.image.load('modules/flakes/resources/window.png')
    fgpicSprite = pyglet.sprite.Sprite(fgpic, 0, 0)
    bgpic = pyglet.image.load('modules/flakes/resources/wintersky.png')
    bgpicSprite = pyglet.sprite.Sprite(bgpic, 0, 0)

    globalVx = random.randrange(20, 80)
    if (random.random() < 0.5):
        globalVx = -1*globalVx

    #print('DLM: globalVx: '+str(globalVx))
    pyglet.clock.schedule_interval(timerFunc, 1.5)

    reset_level(myWin, main_batch)

#    game_window.set_visible(True)


def reset_level(myWin, main_batch):
    global game_objects, event_stack_size, globalVx

    # Clear the event stack of any remaining handlers from other levels
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1

    things = load.things(num_things, myWin, main_batch)

    # Store all objects that update each frame in a list
    game_objects = things

    # Things to do on the game_objects before kickoff
    for obj in game_objects:
        # Add any specified event handlers to the event handler stack
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            event_stack_size += 1
        obj.vx = (0.4/obj.scale) * globalVx

def timerFunc (dt):
    globalVx = random.randrange(10, 40)
    if (random.random() < 0.5):
        globalVx = -1*globalVx
    #print('DLM: timerFunc():globalVx: '+str(globalVx))
    for obj in game_objects:
        obj.vx = (0.4/obj.scale) * globalVx
        #print('DLM: timerFunc: obj.scale: '+str(obj.scale)+' obj.vx:'+str(obj.vx))


# @game_window.event
# def on_draw():
#     game_window.clear()
#     #bgpicSprite.draw()
#     main_batch.draw()
#     #fgpicSprite.draw()
#     counter.draw()

def update(dt):
    global num_things, globalVx

    # To avoid handling collisions twice ...
    # No collisions here
    for obj in game_objects:
        obj.update(dt)

def alldone(dt):

    #print('DLM: Flake: All Done.  Returning Control.')
    pyglet.app.exit()

def main(duration):
    #print('DLM:main:Start')
    # Start it up!
    init()
    #print('DLM:main:Post-Start')

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.clock.schedule_interval(alldone, duration)

    # Tell pyglet to do its thing
    #print('DLM:main:Pre-app.run')
    pyglet.app.run()
    #print('DLM:main:End')
