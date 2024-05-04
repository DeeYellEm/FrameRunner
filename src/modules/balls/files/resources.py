import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# Tell pyglet where to find the resources
pyglet.resource.path = ['modules/balls/resources']
pyglet.resource.reindex()

ball_image = pyglet.resource.image("beachball.png")
center_image(ball_image)
