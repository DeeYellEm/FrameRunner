import pyglet
import random
from . import ball, resources, util

DLMTest = 0

def balls(num_balls, myWin, batch=None):
    """Generate ball objects with random positions and velocities, not close to the player"""
    balls = []
    for i in range(num_balls):
        #print('DLM: num_balls: '+str(num_balls))
#DLM1        ball_x, ball_y, _ = player_position
#DLM1        while util.distance((ball_x, ball_y), player_position) < 100:
#DLM1            ball_x = random.randint(0, 800)
#DLM1            ball_y = random.randint(0, 600)
        new_ball = ball.Ball(x=0, y=0, batch=batch)
        new_ball.rotation = random.randint(0, 360)

        new_ball.vx, new_ball.vy = random.uniform(0.3, 1.0) * 100, random.uniform(0.3, 1.0) * 100
        if (random.random() < 0.5):
            new_ball.vx = -1*new_ball.vx
        if (random.random() < 0.5):
            new_ball.vy = -1*new_ball.vy
        #print('DLM: new_ball.vx: '+str(new_ball.vx)+' new_ball.vy: '+str(new_ball.vy))

        #print('DLM: ball.width: '+str(new_ball.width)+' ball.height: '+str(new_ball.height))

        ball_x = random.randint((0+int(new_ball.width/2)), (myWin.X-int(new_ball.width/2)))
        ball_y = random.randint((0+int(new_ball.height/2)), (myWin.Y-int(new_ball.height/2)))

        new_ball.x = ball_x
        new_ball.y = ball_y
        new_ball.n = num_balls

        if DLMTest == 1:
            # Set some stuff for test purposes
            if (i == 0):
                new_ball.x = 200
                new_ball.y = 300
                new_ball.vx = 50
                new_ball.vy = 0

            if (i == 1):
                new_ball.x = 400
                new_ball.y = 100
                new_ball.vx = 0
                new_ball.vy = 50

        balls.append(new_ball)
    return balls
