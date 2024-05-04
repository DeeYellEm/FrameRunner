Project: FrameRunner.py

Goals: I have a 800x600 display mounted to a Raspberry Pi that I acquired.  What I was imagining for this project was a series of modules that could cycle on the display over time.  Each module would be unique and graphical in nature.  Bouncing balls, a clock, something with images, etc.

The target language was Python because I don't know it well.  I looked around for a graphics library that was lightweight and landed on Pyglet with some basic testing about how fast the library could render and Pyglet was the easy winner.

Pyglet site: https://pyglet.org/
Pyglet documentation: https://pyglet.readthedocs.io/en/latest/index.html
Pyglet github: https://github.com/pyglet/pyglet
Pyglet version used: v2.10.0

Python version: 3.12.1
Developed on Mac with the intention of taking it to Raspberry Pi/Python

Current Modules:
example and example2 : Just dummy modules used during testing
balls : Four beachballs, random rotation and velocity, bouncing off each other and the walls
flakes : A bunch of randomly sized flakes of snow falling.  Has a basic notion of mass and wind direction.
clock : Very basic time in the lower left corner
starfield : Adapted from an online example of a basicl starfield whizzing by
picslide : Uses a bunch of images (created with Midjourney) sliced in to rectangles and dropped from top to bottom.  Over time they will settle in to their lanes and the columns will fill until the pic is complete



