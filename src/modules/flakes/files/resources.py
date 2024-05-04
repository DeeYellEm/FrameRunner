import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# Tell pyglet where to find the resources
pyglet.resource.path = ['modules/flakes/resources/']
pyglet.resource.reindex()

thing_image = pyglet.resource.image("flake.png")
center_image(thing_image)

background_pic = pyglet.resource.image("window.png")
