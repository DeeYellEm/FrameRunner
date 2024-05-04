# FrameRunner.py - 
import pyglet
import random
from collections import namedtuple

# Supported modules
from modules.example import example
from modules.example2 import example2
from modules.balls import balls
from modules.flakes import flakes
from modules.clock import clock
from modules.starfield import starfield
from modules.picslide import picslide

# Set up a window
myWindow = namedtuple('myWindow', ['X', 'Y'])
myWin = myWindow(800, 600)
game_window = pyglet.window.Window(myWin.X, myWin.Y, visible=True, resizable=False)
#counter = pyglet.window.FPSDisplay(window=game_window)
WindowVisible = 1

main_batch = pyglet.graphics.Batch()

# Set up a label
framerunner_label = pyglet.text.Label(text="Framerunner!", x=400, y=575, anchor_x='center', batch=main_batch)
#example.example_label = pyglet.text.Label(text="Example", font_name='Times New Roman', font_size=36, color=(255, 255, 255, 255), x=200, y=300, anchor_x='center', batch=main_batch)

def init():
    #print('DLM: init')

    # Schedule a timer to run every so often (in seconds)
    # t_interval = 1.0
    # pyglet.clock.schedule_interval(timerFunc, t_interval)

    reset_module()


def reset_module():
    global foo
    # Clear any necessary stuff

#def timerFunc (dt):
    # Timer related stuff
    #print('DLM: timerFunc called.')
    #framerunner_label.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)

@game_window.event
def on_close():
    global WindowVisible
    #print('========== DLM: on_window_close() ==========')
    WindowVisible = 0
    game_window.close()

@game_window.event
def on_key_press(symbol, modifier):
    global WindowVisible
    #print("========== DLM: Key Press ==========")
    # key "C" get press
    if symbol == pyglet.window.key.Q:
        WindowVisible = 0
        # close the window
        game_window.close()

@game_window.event
def on_draw():

    game_window.clear()

    main_batch.draw()

    # Test - FPS Counter Display
    #counter.draw()

def update(dt):
    global moduleName
    # Things to do every graphics update cycle, currently set in schedule_interval to 120x per second
    match moduleName:
        case "example":
            example.update(dt, framerunner_label)
        case "example2":
            example2.update(dt, framerunner_label)
        case "balls":
            balls.update(dt)
        case "flakes":
            flakes.update(dt)
        case "clock":
            clock.update(dt, main_batch)
        case "starfield":
            starfield.update(dt)
        case "picslide":
            picslide.update(dt, main_batch, myWin)

#def alldone(dt):
    # Things to do when we're all done.
    #print('DLM: Framerunner: All Done.  Returning Control.')

def main():

    global WindowVisible, moduleName

    typ_dur = 5
    typ_pic = 1

    #print('DLM: FrameRunner...')

    #print('DLM:main:Start')
    # Start it up!
    init()
    #print('DLM:main:Post-Start')

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)


    module_list = ['flakes', 'clock', 'balls', 'starfield', 'picslide']

    while (WindowVisible):
        moduleName = random.choice(module_list)

        # Test: Force the choice
        moduleName = "picslide"
        # Test: Bounce between two
        # if ((count % 2) == 0):
        #     mod = "example"
        # else:
        #     mod = "example2"

        match moduleName:
            case "example":
                #print("DLM: Calling example...")
                duration = 5
                example.init(main_batch, framerunner_label)
                pyglet.clock.schedule_interval(example.alldone, duration)
                #print("DLM: Returned from example...")
            case "example2":
                #print("DLM: Calling example2...")
                duration = 5
                example2.init(main_batch, framerunner_label)
                pyglet.clock.schedule_interval(example2.alldone, duration)
                #print("DLM: Returned from example2...")
            case "balls":
                #print("DLM: Calling Balls...")
                duration = 5
                balls.init(main_batch, myWin)
                pyglet.clock.schedule_interval(balls.alldone, duration)
                #print("DLM: Returned from Balls...")
            case "flakes":
                #print("DLM: Calling Flakes...")
                duration = 5
                flakes.init(main_batch, myWin)
                pyglet.clock.schedule_interval(flakes.alldone, duration)
                #print("DLM: Returned from Flakes...")
            case "clock":
                #print("DLM: Calling Clock...")
                duration = 5
                clock.init(main_batch, myWin)
                pyglet.clock.schedule_interval(clock.alldone, duration)
                #print("DLM: Returned from Clock...")
            case "starfield":
                #print("DLM: Calling Starfield...")
                duration = 5
                starfield.init(main_batch)
                pyglet.clock.schedule_interval(starfield.alldone, duration)
                #print("DLM: Returned from Starfield...")
            case "picslide":
                #print("DLM: Calling Picslide...")
                duration = 1 # For this module, the "duration" is the number of pics reassembled
                picslide.init(main_batch, myWin, duration)
                #pyglet.clock.schedule_interval(picslide.alldone, duration)
                #print("DLM: Returned from Picslide...")
            case _:
                print("DLM: Unmatched case in switch statement.")

        # Tell pyglet to do its thing
        #print('DLM:main:Pre-app.run')
        pyglet.app.run()
        #print('DLM:main:End')

    #print('DLM: Return from sub-call')
    exit(0)

if __name__ == "__main__":
    main()

