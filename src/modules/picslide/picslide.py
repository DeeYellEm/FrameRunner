import pyglet
from pyglet import image
#from pyglet.gl import *

from modules.picslide.files import thing, load, resources
from collections import namedtuple
import random, os, glob, time


# Set up a window
# myWindow = namedtuple('myWindow', ['X', 'Y'])
# myWin = myWindow(800, 600)
# game_window = pyglet.window.Window(myWin.X, myWin.Y, visible=False, resizable=False)
# counter = pyglet.window.FPSDisplay(window=game_window)

# main_batch = pyglet.graphics.Batch()

myTile = namedtuple('myTile', ['X', 'Y'])
myTileSize = myTile(100, 75)


game_objects = []

all_pics = []
pic_tiles = []
pic_count = 0
pic_counter = 0

def init(main_batch, myWin, duration):
    global pic_count
    pic_count = duration
    #print('DLM: PicSlide : We are doing ', str(pic_count), ' of these.')
    # Set up the two top labels
    level_label = pyglet.text.Label(text="Testing - PicSlide!", x=400, y=575, anchor_x='center', batch=main_batch)

    reset_level(main_batch, myWin)

def reset_level(main_batch, myWin):
    global num_things, all_pics, pic_tiles, game_objects

    num_things = int(myWin.X/myTileSize.X * myWin.Y/myTileSize.Y)
    #print('DLM: num_things: '+str(num_things))

    # list to store filename present in current directory
    files = []
    relevant_path = "modules/picslide/resources"
    #print("DLM: relevant_path: "+str(relevant_path))
    included_prefix = ['deeyellem']
    files = [fn for fn in os.listdir(relevant_path)
              if any(fn.startswith(ext) for ext in included_prefix)]
    #    if os.path.isfile(os.path.join('../resources', file_path)):
    #        files.append(str('../resources/'+file_path))
            #print("DLM: Adding file_path: "+str(file_path))
    #for file in files:
        #print('DLM: resource images: '+str(file))

    img_path = relevant_path+'/'+random.choice(files)
    #print("DLM: Random Image: "+img_path)
    img = pyglet.image.load(img_path)

    # Load up the tiles
    pic_tiles = load.things(num_things, myWin, main_batch)

    # Set some tile-related info
    i, j = 0,0
    for tile in pic_tiles:
        picTile = img.get_region(x=(i*myTileSize.X), y=(j*myTileSize.Y), width=myTileSize.X, height=myTileSize.Y)
        tile.image = picTile

        # These locations are where they go in the original image
        #tile.x = i*myTileSize.X
        #tile.y = j*myTileSize.Y
        # Choose some random starting locations
        tile.x = random.randrange(0, myWin.X)
        #tile.y = random.randrange(700, 1200)
        tile.y = random.randrange(100, 600)

        # We'll test against these later to see if a tile made it home
        tile.homex = i*myTileSize.X
        tile.homey = j*myTileSize.Y

        tile.vx = 0
        tile.vy = random.randrange(-160, -75)

        i += 1
        if i == 8:
            j += 1
            i = 0

    game_objects = pic_tiles


#def timerFunc (dt):
#    globalVx = random.randrange(20, 80)
#    if (random.random() < 0.5):
#        globalVx = -1*globalVx
#    print('DLM: timerFunc():globalVx: '+str(globalVx))
#    for obj in game_objects:
#        obj.vx = (0.4/obj.scale) * globalVx
#        #print('DLM: timerFunc: obj.scale: '+str(obj.scale)+' obj.vx:'+str(obj.vx))


# @game_window.event
# def on_draw():
#     game_window.clear()
#     #bgpicSprite.draw()
#     main_batch.draw()
#     #fgpicSprite.draw()
#     counter.draw()

def update(dt, main_batch, myWin):
    global game_objects, pic_count, pic_counter

    DeadCount = 0
    for obj in game_objects:
        obj.update(dt)

        if (obj.dead is False):
            # See if a tile made it home
            if obj.x == obj.homex:
                # If the tile is in the right row (or just under)
                objIndex = game_objects.index(obj)
                #print('DLM: picslide:update:objIndex: '+str(objIndex))
                #if (objIndex < 8):
                #    obj.opacity = random.randrange(160, 255)
                if (obj.homey == obj.y) or ((obj.y < obj.homey) and (obj.homey-obj.y < 5)) :
                    # In case the y gets incremented by more than one, the above says if it's at or less than 5 pixels below
                    #print('DLM: obj.y: '+str(obj.y)+' obj.homey: '+str(obj.homey))
                    # If the tile below is dead or there's no tile below

                    if (objIndex < 8):
                        # One of the bottom row tiles
                        obj.dead = True
                        obj.y = obj.homey
                        #obj.opacity = 128
                        #print('DLM: picslide:update:Home? True for objIndex('+str(objIndex)+') on the bottom')
                    else:
                        objBelow = game_objects[objIndex-8]
                        #print('DLM: picslide:update:objBelowIndex: '+str(objIndex-8))

                        if objBelow.dead is True:
                            obj.dead = True
                            obj.y = obj.homey
                            #obj.opacity = 128
                            #print('DLM: picslide:update:Home? True for objIndex('+str(objIndex)+') on another tile')
        else:
            DeadCount +=1

        if DeadCount == 64:
            #print('DLM:update: DeadCount == 64 - Pic is done.')
            time.sleep(5.0)
            reset_level(main_batch, myWin)
            pic_counter += 1
            #print("DLM: update: pic_counter = "+str(pic_counter)+" pic_count = "+str(pic_count))
            # This is where we exit if the pic_counter is equal to the pic_count
            if (pic_counter == pic_count):
                pyglet.app.exit()
                #print('DLM: All Done.  Returning Control.')
                

# def alldone(dt):
#     print('DLM: PicSlide: All Done.  Returning Control.')
#     pyglet.app.exit()


def main(pc):
    global pic_count

    pic_count = pc
    # Start it up!
    init()

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    #pyglet.clock.schedule_interval(alldone, duration)

    # Tell pyglet to do its thing
    pyglet.app.run()
