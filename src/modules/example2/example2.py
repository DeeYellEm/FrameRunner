import pyglet
import time
#from pyglet import image
#from pyglet.gl import *

#import random

# Set up a window
#myWindow = namedtuple('myWindow', ['X', 'Y'])
#myWin = myWindow(800, 600)
#game_window = pyglet.window.Window(myWin.X, myWin.Y, visible=False, resizable=False)
#counter = pyglet.window.FPSDisplay(window=game_window)

#main_batch = pyglet.graphics.Batch()

# Global Wind
#globalVx = 0.0

#game_objects = []

# We need to pop off as many event stack frames as we pushed on
# every time we reset the level.
event_stack_size = 0

#main_batch = pyglet.graphics.Batch()

#example_label = pyglet.text.Label("Example", x=200, y=300, anchor_x='center', batch=main_batch)
#example_label = pyglet.text.Label(text="Fafhrd", font_name='Times New Roman', font_size=36, color=(255, 255, 255, 255), x=200, y=300, anchor_x='center', batch=main_batch)
#example_label = pyglet.text.Label("Example", x=200, y=300, anchor_x='center')

def init(main_batch, framerunner_label):
    global example_label
    #global num_things, fgpic, fgpicSprite, bgpic, bgpicSprite, globalVx
    #global game_window

    print('== DLM: example2:init()')

    # Set up the top label
    example_label = pyglet.text.Label(text="Example2", x=200, y=300, color=(255, 255, 255, 255), anchor_x='center', batch=main_batch)
    framerunner_label.text = "Falafel!!"
    example_label.text = "Now Example2"
    example_label.draw()

    # Schedule a timer to run every so often (in seconds)
    t_interval = 1.0
    #pyglet.clock.schedule_interval(timerFunc, t_interval)

    reset_level()


def reset_level():
    global foo

    # Clear any necessary stuff

def timerFunc (dt):
    foo = 0
    print('DLM: Example2:timerFunc called.')
    # timerFunc Stuff

#@game_window.event
#def on_draw():

def update(dt, framerunner_label):
    global foo

    # Thing to update
    tmp = framerunner_label.y
    framerunner_label.y = tmp - 1
    if framerunner_label.y == 0:
        framerunner_label.y = 575

def alldone(dt):

    print('DLM: Example2: All Done.  Returning Control.')
    pyglet.app.exit()
