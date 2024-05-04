import pyglet, time
from modules.balls.files import ball, load
from collections import namedtuple

# Set up a window
#myWindow = namedtuple('myWindow', ['X', 'Y'])
#myWin = myWindow(800, 600)
#game_window = pyglet.window.Window(myWin.X, myWin.Y, visible=False, resizable=False)
#counter = pyglet.window.FPSDisplay(window=game_window)
#
#main_batch = pyglet.graphics.Batch()

# Set up the two top labels
#score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
#level_label = pyglet.text.Label(text="Testing - Balls!", x=400, y=575, anchor_x='center', batch=main_batch)

game_objects = []
num_balls = 4

# We need to pop off as many event stack frames as we pushed on
# every time we reset the level.
event_stack_size = 0

def init(main_batch, myWin):
    global num_balls

    #print('== DLM: balls:init()')
    # Set up the top label
    balls_label = pyglet.text.Label(text="Balls", x=200, y=300, color=(255, 255, 255, 255), anchor_x='center', batch=main_batch)
    balls_label.draw()

    num_balls = 4
    reset_level(main_batch, myWin)

def reset_level(main_batch, myWin):
    global game_objects, event_stack_size

    balls = load.balls(num_balls, myWin, main_batch)

    # Store all objects that update each frame in a list
    game_objects = balls

    # Add any specified event handlers to the event handler stack
    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            event_stack_size += 1


#@game_window.event
#def on_draw():
#    game_window.clear()
#    main_batch.draw()
#    counter.draw()

def update(dt):
    global num_balls

    # To avoid handling collisions twice, we employ nested loops of ranges.
    # This method also avoids the problem of colliding an object with itself.
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):

            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            # Make sure the objects haven't already been killed
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    #print('DLM: Obj1 collides with Obj2')


    # Let's not modify the list while traversing it
    to_add = []

    for obj in game_objects:
        obj.update(dt)

        to_add.extend(obj.new_objects)
        obj.new_objects = []

def alldone(dt):
    #print('DLM: Ball: All Done.  Returning Control.')
    pyglet.app.exit()

# def main(duration):
#     print('DLM:balls:main:Start')
#     # Start it up!
#     init()

#     # Update the game 120 times per second
#     pyglet.clock.schedule_interval(update, 1 / 120.0)

#     pyglet.clock.schedule_interval(alldone, duration)

#     # Tell pyglet to do its thing
#     pyglet.app.run()
#     print('DLM:main:End')
