import pyglet
from pyglet import image
from pyglet.gl import *

from datetime import datetime, date

from collections import namedtuple

# Set up a window
# myWindow = namedtuple('myWindow', ['X', 'Y'])
# myWin = myWindow(800, 600)
# game_window = pyglet.window.Window(myWin.X, myWin.Y, visible=False, resizable=False)
# main_batch = pyglet.graphics.Batch()
# event_loop = pyglet.app.EventLoop()

def init(main_batch, myWin):

    #print('DLM: init:game_window.visible')
    # Make the window for this module visible
    #game_window.set_visible(True)
    #print('DLM: init:game_window.visible is: '+str(game_window.visible))

    # We need to pop off as many event stack frames as we pushed on
    # every time we reset the level.
    event_stack_size = 0

    # Set up labels
    level_label = pyglet.text.Label(text="Testing - Clock!", x=400, y=575, anchor_x='center', batch=main_batch)

    # Set up the time/date Labels offscreen
    time_label = pyglet.text.Label(text="Time", x=100, y=-300, anchor_x='left', batch=main_batch, font_size=48)
    date_label = pyglet.text.Label(text="Date", x=100, y=-400, anchor_x='left', batch=main_batch, font_size=48)

#    counter = pyglet.window.FPSDisplay(window=game_window)

# @event_loop.event
# def on_window_close(window):
#     event_loop.exit()

# @game_window.event
# def on_draw():
#     game_window.clear()
#     #bgpicSprite.draw()
#     main_batch.draw()
#     #fgpicSprite.draw()
#     #counter.draw()

def update(dt, main_batch):
    global time_label, level_label, date_label

    # Called to update time per second
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    #print("Current Time =", current_time)
    time_label = pyglet.text.Label(text=current_time, x=40, y=60, anchor_x='left', batch=main_batch, font_size=72)
    today = date.today()
    # Textual month, day and year
    strdate = today.strftime("%m/%d/%y")
    date_label = pyglet.text.Label(text=strdate, x=70, y=20, anchor_x='left', batch=main_batch, font_size=36)

def alldone(dt):
    #print('DLM: Clock: All Done.  Returning Control.')
    pyglet.app.exit()

def main(duration):
    #print('DLM:main:Start')
    # Start it up!
    init()

    # Update the clock every second
    pyglet.clock.schedule_interval(update, 1.0)

    pyglet.clock.schedule_interval(alldone, duration)


    # Tell pyglet to do its thing
    pyglet.app.run()
    #print('DLM:main:End')

